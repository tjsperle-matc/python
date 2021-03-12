#!/usr/bin/env python3

print("Name:Tyler Sperle")

print("")

Total = 0

keywords = ["gmeach18@ed.gov", "dcassyqw@microsoft.com", "Whiteland", "Kayley", 
"248.253.63.149", "80.222.19.190"]

file = open("Midterm-if.txt", "r")

data = file.readlines()
for line in data:
    for key in keywords:

        if key in line:
            words = line.split(",")
            Total += int(words[0])

print(f"The total is: {Total}")
file.close()
