from sys import argv

from bitarray import bitarray


def primes(n: int):
    """
    Generate prime numbers using Eratosthenes sieve.
    :param n: upper bound
    :return: generator of prime numbers from 2 to n including
    """

    if (n < 2): return ()
    sieve = bitarray(n-2+1)
    sieve.setall(True)

    p = 1
    try:
        while p < n+1:
            p = next(x for x in range(p+1, n+1) if sieve[x-2])
            for j in range(p+p, n+1, p):
                sieve[j-2] = False
    except StopIteration:
        pass
    return (i+2 for i in range(n-2+1) if sieve[i])


if __name__ == "__main__":
    print(*primes(int(argv[1])))
