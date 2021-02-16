#!/usr/bin/env python3

varString = "Here is a nice string to slice"
varList = [ "Here", "is", "a", "nice", "list", "to", "slice" ] 

print(f"{varString}"[3:]), print(f"{varString}"[:-27]), print(f"{varString}"[3:][:-18]), print(f"{varString}"[::2]), print(f"{varString}"[::-1])

print("")

print(varList[::-1]), print(varList[2::-1]), print(varList[2:4]), print(varList[::3]), print(varList[1:7])

print("")

# for element in varString:
	# None

for thing in varString:
	#print(f"{element}")
	print(f"{thing}")

print("")

# for element in varList
	# None

for thing in varList:
	#print(f"{element}")
	print(f"{thing}")
