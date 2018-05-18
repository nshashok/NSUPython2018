import math

def is_prime(n: int):
    if (n <= 1 or (n > 2 and n&1 == 0)):
        return False
    if (n == 2):
        return True

    for k in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % k == 0):
            return False

    return True

def generate_primes(upper_border):
    return [number for number in range(2, int(upper_border)+1) if is_prime(number)]

if (__name__ == "__main__"):
    print(generate_primes(100))
