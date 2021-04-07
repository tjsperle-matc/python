#!/usr/bin/env python3

def f2c(temperature):
    return (temperature - 32) * 5/9

def main():
    degrees_fahrenheit = int(input("Enter a temperature in degrees Fahrenheit: "))
    print(f"The temperature in degrees Celsius is: {f2c(degrees_fahrenheit)}")

if __name__ == "__main__":
    main()
