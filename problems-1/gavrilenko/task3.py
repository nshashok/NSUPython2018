import math
from bitarray import bitarray


def eratosthenesArray(n):
    array = [True] * (n + 1)
    array[0] = array[1] = False

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if array[i]:
            for j in range(i ** 2, n + 1, i):
                array[j] = False
    return [i for i in range(2, n + 1) if array[i]]


def eratosthenesBitearray(n):
    array = bitarray(n + 1)
    array.setall(True)
    array[0] = array[1] = False

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if array[i]:
            for j in range(i ** 2, n + 1, i):
                array[j] = False
    return [i for i in range(2, n + 1) if array[i]]


def eratosthenesSet(n):
    array = set(range(2, n + 1))

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if i in array:
            for j in range(i ** 2, n + 1, i):
                array.discard(j)
    return array

