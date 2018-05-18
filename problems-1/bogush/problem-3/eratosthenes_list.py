from sys import argv


def primes(n: int):
    """
    Generate prime numbers using Eratosthenes sieve.
    :param n: upper bound
    :return: generator of prime numbers from 2 to n including
    """
    sieve = list(range(2, n+1))

    p = 1
    try:
        while p < n+1:
            p = next(sieve[i] for i in range(p-1, n-1) if sieve[i] > 0)
            for j in range(p+p-2, n-1, p):
                sieve[j] = -abs(sieve[j])
    except StopIteration:
        pass
    return (x for x in sieve if x > 0)


if __name__ == "__main__":
    print(*primes(int(argv[1])))
