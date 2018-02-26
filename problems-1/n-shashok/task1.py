def prime_factors(n):
    dd = 2
    nn = n
    fact = []
    while dd <= nn:
        c = 0
        while (nn % dd) == 0:
            c += 1
            nn /= dd
        if c != 0:
            fact.append([dd, c])
        dd += 1
    return fact
