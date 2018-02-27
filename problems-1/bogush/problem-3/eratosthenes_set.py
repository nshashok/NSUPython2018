from sys import argv


def primes(n: int):
    """
    Generate prime numbers using Eratosthenes sieve.
    :param n: upper bound
    :return: generator of prime numbers from 2 to n including
    """
    sieve = set(range(2, n+1))

    p = 1
    try:
        while p < n+1:
            p = next(x for x in range(p+1, n+1) if x in sieve)
            for j in range(p+p, n+1, p):
                if j in sieve:
                    sieve.remove(j)
    except StopIteration:
        return (x for x in sieve if x > 0)
    return sieve


primes(int(argv[1]))
