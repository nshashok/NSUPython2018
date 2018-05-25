import unittest

def get_prime_factorization(number: int):
    if (type(number) != int):
        raise TypeError("Expected integer type, got: " + str(type(number)))
    if (number <= 0):
        raise ValueError("Expected a positive integer, got: " + str(number))
        
    factors = []
    factor = 2

    while (number > 1):
        power = 0
        while (number % factor == 0):
            power += 1
            number //= factor
        if (power > 0):
            factors.append([factor, power])
        factor += 1

    return factors


class TestPrimeFactorization(unittest.TestCase):
    def test_surpress_non_positive_number_input(self):
        with self.assertRaises(ValueError):
            get_prime_factorization(-1)

        with self.assertRaises(ValueError):
            get_prime_factorization(0)

    def test_surpress_invalid_types_input(self):
        with self.assertRaises(TypeError):
            get_prime_factorization(set())

        with self.assertRaises(TypeError):
            get_prime_factorization(list())

        with self.assertRaises(TypeError):
            get_prime_factorization(str())

    def test_powers(self):
        self.assertEqual(get_prime_factorization(128), [[2,7]])
        self.assertEqual(get_prime_factorization(9), [[3,2]])
        self.assertEqual(get_prime_factorization(225), [[3,2], [5, 2]])
        self.assertEqual(get_prime_factorization(282475249), [[7,10]])

    def test_prime_numbers(self):
        self.assertEqual(get_prime_factorization(2), [[2,1]])
        self.assertEqual(get_prime_factorization(5), [[5,1]])
        self.assertEqual(get_prime_factorization(53), [[53,1]])
        self.assertEqual(get_prime_factorization(997), [[997,1]])

    def test_one(self):
        self.assertEqual(get_prime_factorization(1), [])

    def test_various(self):
        self.assertEqual(get_prime_factorization(12344), [[2, 3], [1543, 1]])
        self.assertEqual(get_prime_factorization(3628800), [[2, 8], [3, 4], [5, 2], [7, 1]])

if __name__ == "__main__":
    try:
        unittest.main()
    except Exception as e:
        print(e)
