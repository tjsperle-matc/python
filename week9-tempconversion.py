#!/usr/bin/env python3

from f2c import f2c
from c2f import c2f

def main():
    temp = int(input("Please input a temperature: "))
    measure = input("Is this temperature in degrees Fahrenheit (f) or Celsius (c)? ")
    if measure == "f":
        print(f"The temperature in degrees Celsius is: {f2c(temp)}")
    if measure == "c":
        print(f"The temperature in degrees Fahrenheit is: {c2f(temp)}") 

if __name__ == "__main__":
    main()
