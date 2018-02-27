import unittest
from functools import reduce

from prime import is_prime
from factorize import factorize


class TestFactorize(unittest.TestCase):
    first_25_primes = {+2, +3, +5, +7, 11,
                       13, 17, 19, 23, 29,
                       31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71,
                       73, 79, 83, 89, 97}

    def test_is_prime(self):
        for n in range(100):
            if n in self.first_25_primes:
                self.assertTrue(is_prime(n), "{} must be prime".format(n))
            else:
                self.assertFalse(is_prime(n), "{} must be non-prime".format(n))

    def test_factorize(self):
        for n in range(2, 100):
            product = reduce(lambda r, f: r * (f[0] ** f[1]), factorize(n), 1)
            self.assertTrue(n == product,
                            "{} != {}, i.e. product of its factorization".format(n, product))
