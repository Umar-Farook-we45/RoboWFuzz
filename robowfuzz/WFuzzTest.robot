*** Settings ***
Library  RoboWFuzz  lists/directory-list-1.0.txt

*** Test Cases ***
Directory Bruter
    [Timeout]  15 minutes
    brute_directories  http://testphp.vulnweb.com/FUZZ  concur=6  follow=True