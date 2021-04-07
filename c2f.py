#!/usr/bin/env python3

def c2f(temperature):
    return (temperature * 9/5) + 32

def main():
    degrees_celsius = int(input("Enter a temperature in degrees Celsius: "))
    print(f"The temperature in degrees Fahrenheit is: {c2f(degrees_celsius)}")

if __name__ == "__main__":
    main()

