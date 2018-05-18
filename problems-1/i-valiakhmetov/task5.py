#!/bin/python

import unittest

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

def primes(n):
	return [x for x in range(2, n+1) if is_prime(x)]
	
class Test_is_prime(unittest.TestCase):
    def test1(self):
        self.assertEqual(primes(0), [])
        self.assertEqual(primes(1), [])
        self.assertEqual(primes(2), [2])
        self.assertEqual(primes(3), [2, 3])

    def test2(self):
        self.assertEqual(primes(10), [2, 3, 5, 7])
        self.assertEqual(primes(13), [2, 3, 5, 7, 11, 13])

if __name__ == "__main__":
	unittest.main()