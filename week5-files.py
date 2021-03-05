#!/usr/bin/env python3

hFile = open("/etc/passwd", "r")
strfiletext = hFile.read()
print(strfiletext)
print("")
print(type(strfiletext))
print("")
print(f"len() function counts the amount of characters: {len(strfiletext)}")
hFile.close()

print("\nUse this technique to display the output of a file as a string and read the length of the string\n")

hFile = open("/etc/passwd", "r")
listfiletext = hFile.readlines()
print(listfiletext)
print("")
print(type(listfiletext))
print("")
print(f"len() function counts the amount of list items: {len(listfiletext)}")
hFile.close()

print("\nUse this technique when trying to display the output of a file in a list while counting the amount of list items\n")

gecosCharacters = 0

with open('/etc/passwd', 'r') as passwdFile:

    try:

        while True:
            currentGecos = next(passwdFile)
            print(f"The value of currentGecos is:\n{currentGecos}")
            gecosCharacters = gecosCharacters + len(currentGecos)

    except StopIteration:
        print(f"The total number of characters is {gecosCharacters}")

print("\nUse this technique when writing a password cracker or sorting through a file list\n")

