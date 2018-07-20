*** Settings ***
Library  RoboWFuzz  /home/umar/Desktop/ThreadPlayBook-Dev/Tools/RoboWFuzz-master/lists/directory-list-2.3-small.txt

*** Variable ***
${REPORT}   /home/umar/Desktop/ThreadPlayBook-Dev/Tools/RoboWFuzz-master/report_nikto.json

*** Test Cases ***
Directory Bruter
    [Timeout]  3 minutes
    brute_directories  http://104.236.85.150/FUZZ   6    ${REPORT}  json   False