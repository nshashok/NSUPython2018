import math

def ifPrime(x):

	if x < 2:

		return False

	for i in range(2, math.floor(math.sqrt(x)) + 1):

		if x % i == 0:

			return False

	return True

for i in range(-3, 101):
	print(i, ifPrime(i))
