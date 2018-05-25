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

class Test_is_prime(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(271), True)

    def test2(self):
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(3*7), False)

if __name__ == "__main__":
	unittest.main()
