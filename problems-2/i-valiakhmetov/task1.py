#!/bin/python

s = None

while not isinstance(s, int):
	try:
		s = int(input("Enter a number: "))
	except ValueError:
		pass
	except EOFError:
		break

print("\nEntered number: ", s, "\nexiting...")
