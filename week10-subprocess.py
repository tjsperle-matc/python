#!/usr/bin/env  python3

import subprocess

CompletedProcess = subprocess.run(["ps","-axco","command"], stdout=subprocess.PIPE)

myProc = CompletedProcess.stdout

myProcString = myProc.decode()

myProcList = myProcString.split('\n')

print(f"The number of processes in this list is:",int(len(myProcList[1:])))

for list in (myProcList[1:][:-1]):
    print(f"{list}")
