# dynamics-setsparser
A little python script to parse odat sets from Microsoft Dynamics's Organization.svc

Example of usage:

```./setsparser.py https://example.com/CRM/XRMServices/2011/OrganizationData.svc/ --login 'corp\JSmith' --password 'verys3cr3tPass'```

Script will save all the sets in timestamp directory, every set in it's own file, beautified with json library
