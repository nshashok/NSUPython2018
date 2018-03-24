import sys


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

if __name__ == "__main__":
    while True:
        try:
            num = input("Enter num: ")
            print(prime_factors(int(num)))
            break
        except ValueError:
            print("\tCan't parse value", file=sys.stderr)
