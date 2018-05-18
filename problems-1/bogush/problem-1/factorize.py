def factorize(n):
    """
    Produces the prime factorization of n.
    :return: list of pairs [p, k] where:
        p is the prime factor
        k is the power of p in factorization
    """
    factors = []
    factor = 2
    while n > 1:
        power = 0
        while n > 1:
            quotient = n // factor
            rest = n - quotient * factor
            if rest > 0:
                break
            n = quotient
            power += 1
        if power > 0:
            factors.append([factor, power])
        factor += 1
    return factors
