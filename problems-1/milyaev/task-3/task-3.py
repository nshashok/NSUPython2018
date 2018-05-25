import math
import unittest
import bitarray
import time


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    if n < 2:
        return False
    max_factor = int(math.sqrt(n))
    return all(n % i for i in range(3, max_factor + 1, 2))


def eratosthenes_list(n):
    sieve = [True] * n
    max_factor = int(math.sqrt(n))

    for i in range(2, max_factor + 1):
        if sieve[i]:
            for j in range(2 * i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]


def eratosthenes_set(n):
    sieve = set(range(2, n))
    max_factor = int(math.sqrt(n))

    for i in range(2, max_factor + 1):
        if i in sieve:
            for j in range(2 * i, n, i):
                if j in sieve:
                    sieve.remove(j)
    return sieve


def eratosthenes_bitarray(n):
    sieve = bitarray.bitarray(n)
    sieve.setall(True)
    max_factor = int(math.sqrt(n))

    for i in range(2, max_factor + 1):
        if sieve[i]:
            for j in range(2 * i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]


def measure_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time


def test_time(sieve_size):
    print("List: {:.4f}".format(measure_time(eratosthenes_list, sieve_size)))
    print("Set: {:.4f}".format(measure_time(eratosthenes_set, sieve_size)))
    print("Bitarray: {:.4f}".format(measure_time(eratosthenes_bitarray, sieve_size)))


class TestEratosthenes(unittest.TestCase):
    n = 1000
    N = 10_000_000

    def test_list(self):
        self.assertTrue(all((not is_prime(i) and i not in eratosthenes_list(self.n)) or
                            (is_prime(i) and i in eratosthenes_list(self.n))
                            for i in range(self.n)))

    def test_set(self):
        self.assertTrue(all((not is_prime(i) and i not in eratosthenes_set(self.n)) or
                            (is_prime(i) and i in eratosthenes_set(self.n))
                            for i in range(self.n)))

    def test_bitarray(self):
        self.assertTrue(all((not is_prime(i) and i not in eratosthenes_bitarray(self.n)) or
                            (is_prime(i) and i in eratosthenes_bitarray(self.n))
                            for i in range(self.n)))


if __name__ == "__main__":
    test_time(10_000_000)
    unittest.main()
