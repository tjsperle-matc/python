#!/usr/bin/env python3

print("Name:Tyler Sperle")

slicingFile = open('slicing-file.txt', 'r')
listfiletext = slicingFile.readlines()
slicingFile.close()

A = listfiletext[24::3]
print(A)

B = listfiletext[2:5]
print(B)

C = listfiletext[12:-9][::-1][::2]
print(C)

D = listfiletext[10:-14]
print(D)

E = listfiletext[6:-18][::-1]
print(E)

quote = (A+B+C+D+E)
print("".join(quote))
