import math


def ifPrime(x):

    if x < 2:

        return False

    for i in range(2, math.floor(math.sqrt(x)) + 1):

        if x % i == 0:

            return False

    return True



def generateList(n):

    return [i for i in range(2, n+1) if ifPrime(i)]



print(generateList(50))
