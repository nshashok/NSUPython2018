#!/bin/python

import unittest

def factor(n):
	a = []
	f = 2

	c = 0
	while n > 1:
		if (n % f == 0):
			c += 1
			n /= f
		else:
			if (c > 0):
				a.append([f, c])
				c = 0
			f += 1
	if (c > 0):
		a.append([f, c])
	return a

class Test_factor(unittest.TestCase):
    def test0(self):
        self.assertEqual(factor(12), [[2, 2], [3, 1]])

    def test1(self):
        self.assertEqual(factor(7), [[7, 1]])

    def test2(self):
        self.assertEqual(factor(7 * 3), [[3, 1], [7, 1]])

    def test3(self):
        self.assertEqual(factor(0), [])
        self.assertEqual(factor(1), [])

if __name__ == "__main__":
	unittest.main()