#!/bin/python

import unittest
from timeit import timeit
from bitarray import bitarray

NN = 100000000

def is_prime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i*i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

def sieve_list(n):
	a = [True] * n
	a[0] = a[1] = False

	for i in range(2, int(n ** .5) + 1):
		if a[i]:
			for j in range (i*i, n, i):
				a[j] = False
	return [i for i in range(2, n) if a[i]]

def sieve_set(n):
    a = set(range(2, n))
    for i in range(2, int(n ** .5) + 1):
        for j in range(i*i, n, i):
            a.discard(j)
    return a

def sieve_bitarray(n):
    a = bitarray(n)
    a.setall(True)

    for i in range(2, int(n ** .5) + 1):
        for j in range(i*i, n, i):
            a[j] = False
    return [i for i in range(2, n) if a[i]]
	
def wrapper_sieve_list():
	return sieve_list(NN)

def wrapper_sieve_set():
	return sieve_set(NN)

def wrapper_sieve_bitarray():
	return sieve_bitarray(NN)
	
class Test_is_prime(unittest.TestCase):
    def test1(self):
		a = [x for x in range(2, 1000) if is_prime(x)]
		self.assertEqual(sieve_list(1000), a)
		self.assertEqual(sieve_set(1000), set(a))
		self.assertEqual(sieve_bitarray(1000), a)

    def test2(self):
		self.assertEqual(sieve_list(2), [])
		self.assertEqual(sieve_set(2), set([]))
		self.assertEqual(sieve_bitarray(2), [])

if __name__ == '__main__':
	unittest.main()
	time = timeit(wrapper_sieve_set, number=1000)
	print("set: ",time)
	time = timeit(wrapper_sieve_bitarray, number=1000)
	print("bitarray: ",time)
	time = timeit(wrapper_sieve_list, number=1000)
	print("list: ",time)
	

