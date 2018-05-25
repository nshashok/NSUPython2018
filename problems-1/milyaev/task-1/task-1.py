import math
import unittest


def prime_factors(n):
    factors = []
    current_factor = 2
    max_factor = math.ceil(math.sqrt(n))
    while n != 1 and current_factor < max_factor:
        degree = 0
        while n % current_factor == 0:
            n //= current_factor
            degree += 1
        if degree > 0:
            factors.append([current_factor, degree])
        current_factor += 1
    if n > 1:
        factors.append([n, 1])
    return factors


class TestPrimeFactors(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(prime_factors(0), [])

    def test_one(self):
        self.assertEqual(prime_factors(1), [])

    def test_prime(self):
        self.assertEqual(prime_factors(17), [[17, 1]])

    def test_composite(self):
        self.assertEqual(prime_factors(2 ** 3 * 5 ** 4 * 17 ** 2), [[2, 3], [5, 4], [17, 2]])

    def test_big_prime(self):
        self.assertEqual(prime_factors(2 ** 31 - 1), [[2 ** 31 - 1, 1]])


if __name__ == "__main__":
    unittest.main()
