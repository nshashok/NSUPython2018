import math

def erArray(n):
	array = [True] * (n + 1)
	array[0] = False
	array[1] = False

	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if array[i]:
			for j in range(i ** 2, n + 1, i):
				array[j] = False
	return [i for i in range(2, n + 1) if array[i]]

def erBitarray(n):
	array = bitarray(n + 1)
	array.setall(True)
	array[0] = False
	array[1] = False

	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if array[i]:
			for j in range(i ** 2, n + 1, i):
				array[j] = False
	return [i for i in range(2, n + 1) if array[i]]

def erSet(n):
	array = set(range(2, n + 1))

	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if i in array:
			for j in range(i ** 2, n + 1, i):
				array.discard(j)
	return array

print (erSet(1000000))
