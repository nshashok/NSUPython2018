import unittest
import bitarray
import math
import time

def is_prime(n: int):
    if (n <= 1 or (n > 2 and n&1 == 0)):
        return False
    if (n == 2):
        return True

    for k in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % k == 0):
            return False

    return True

def erat_list(n: int):
    numbers = list(range(n))
    result = [2]

    for step in range(3, int(math.sqrt(n))+1, 2):
        if (numbers[step] != 0 and step&1 == 1): result.append(step)
        for k in range(2 * step, n, step):
            numbers[k] = 0

    return result
    # return [k for k in numbers if k >= 2]

def erat_set(n: int):
    if (n <= 1): return []
    numbers = set(range(3, n, 2))
    numbers.add(2)

    for step in range(3, int(math.sqrt(n))+1, 2):
        for k in range(2*step, n, step):
            if (k in numbers):
                numbers.remove(k)

    return list(numbers)

def erat_bitarray(n: int):
    bits = bitarray.bitarray('1') * n
    result = [2]

    for step in range(3, int(math.sqrt(n))+1, 2):
        if (bits[step]): result.append(step)
        for k in range(2 * step, n, step):
            bits[k] = False

    return result


def measure_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


class TestEratosphenus(unittest.TestCase):
    sieve_size = 100000
    large_sieve_size = 10000000

    def test_list_implementation(self):
        self.assertTrue(all([is_prime(number) for number in erat_list(self.sieve_size)]))

    def test_set_implementation(self):
        self.assertTrue(all([is_prime(number) for number in erat_set(self.sieve_size)]))

    def test_bitarray_implementation(self):
        self.assertTrue(all([is_prime(number) for number in erat_bitarray(self.sieve_size)]))

    def test_measure_work_time(self):
        print()
        print("Measuring work time on a large sieve ({} elements)...".format(self.large_sieve_size))
        print("Time test results (seconds): ")
        print("List: {0:.4f}".format(measure_time(erat_list, self.large_sieve_size)))
        print("Set: {0:.4f}".format(measure_time(erat_set, self.large_sieve_size)))
        print("Bitarray: {0:.4f}".format(measure_time(erat_bitarray, self.large_sieve_size)))

if __name__ == '__main__':
    unittest.main()
