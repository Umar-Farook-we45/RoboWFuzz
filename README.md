## RoboWFuzz

Robot Framework Integration for the generic python fuzzing library `wfuzz`

Currently, there's only a single functionality implemented, which is Directory Bruteforcing

`brute directories | url | concur=2 | file_name=exportfile.json | format=json |  follow=False`

- `url`: mandatory param
- `concur`: concurrency, the number of parallel processes that need to be run. optional param
- `file_name`: export file name, default writes to the same directory that you install. Optional Param
- `format` : raw | json (Default: `raw` )
- `follow`: Follow 301 redirects or not, defaults to False. Optional Param

```
*** Settings ***
Library  RoboWFuzz  lists/directory-list-1.0.txt

*** Test Cases ***
Directory Bruter
    [Timeout]  15 minutes
    brute_directories  http://testphp.vulnweb.com/FUZZ  6  json  True

```
