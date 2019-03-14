#!/usr/bin/python3

import argparse
import requests
from requests_ntlm import HttpNtlmAuth
import sys

#dealing with arguments
parser = argparse.ArgumentParser()

parser.add_argument('urlGet', action='store', help='url to get all the sets')
parser.add_argument('-uP', action='store', dest='urlParse', help='url to parse all the contents')
parser.add_argument('--login', action='store', dest='login', help='login to authenticate through ntlm (if needed), for example: corp\JSmith')
parser.add_argument('--password', action='store', dest='password', help='password to login through ntlm')

args = parser.parse_args()

def getSets(url):
    sets = getRequest(args.urlGet)
    return sets['d']['EntitySets']

def getRequest(url, par = None):
    if not par:
        par = {}
    if args.login and args.password:
        r = requests.get(url,auth=HttpNtlmAuth(args.login,args.password),headers={'Accept':'application/json'},params=par)
    else:
        r = requests.get(url,headers={'Accept':'application/json'})
    try:
        result = r.json()
    except:
        print('\nError. Request can\'t get JSON, maybe you need to authenticate? Anyway, here\'s server\'s response:\n')
        print(r.text)
        quit()
    return result

def parseSets(url):
    sets = getSets(url)
    f = open("result.txt","w")
    counter = len(sets)
    doneCounter = 0
    for set in sets:
        f.write('SET NAME: ' + set + '\n')
        f.write('CONTENT:\n')
        f.write(str(getRequest(url + set, par={'$select':'*'})) + '\n\n\n')
        counter -= 1
        doneCounter += 1
        sys.stdout.write('Sets parsed: ' + str(doneCounter) + ' from ' + str(counter) + '\r')
        sys.stdout.flush()
    print('All done!')

def main():
    parseSets(args.urlGet)

if __name__ == "__main__":
    main()
