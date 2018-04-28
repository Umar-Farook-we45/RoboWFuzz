*** Settings ***
Library  /Users/abhaybhargav/Documents/Code/Python/RoboWFuzz/robowfuzz/RoboWFuzz.py  /Users/abhaybhargav/Documents/Code/Python/RoboWFuzz/lists/directory-list-1.0.txt

*** Test Cases ***
Directory Bruter
    [Timeout]  20 seconds
    brute_directories  http://testphp.vulnweb.com/FUZZ  concur=6  follow=True