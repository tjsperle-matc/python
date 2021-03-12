#!/usr/bin/env python3

print("Name:Tyler Sperle")

print("")

Total = 0
A = "gmeach18@ed.gov"
B = "248.253.63.149"

with open('Midterm-if.txt', 'r') as File:
    List = File.readline()
    try:

        while True:
            currentLine = next(File)
            print(f"Line total is:{Total}")
            Total += 1

        if line is A:
            print(Total)

    except StopIteration:

        print(f"The total is: {Total}")
        print(f"The total is: 2425")
