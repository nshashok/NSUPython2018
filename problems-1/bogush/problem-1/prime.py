from math import sqrt
from itertools import count, chain


def is_prime(n):
    """
    Returns True if n is prime and False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes(stop=None):
    """
    Return a generator of prime numbers from 2 to infinity
    or to stop (excluding) if stop is defined.
    """
    if stop is None:
        high_primes = ((p for p in count(start=3, step=2) if is_prime(p)))
    else:
        high_primes = ((p for p in range(3, stop, 2) if is_prime(p)))
    return chain([2], high_primes)
