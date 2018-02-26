import math


def is_prime(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True
