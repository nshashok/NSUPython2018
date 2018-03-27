import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    if n < 2:
        return False
    max_factor = int(math.sqrt(n))
    return all(n % i for i in range(3, max_factor + 1, 2))


def first_prime_numbers(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


if __name__ == "__main__":
    print(first_prime_numbers(100))