import math
from bitarray import bitarray
import task0


def primes_bit_array_2(n):
    a = bitarray((n + 1) * bitarray('1'))
    a[0] = 0
    a[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i] == 1:
            for k in range(i + i, n + 1, i):
                a[k] = 0
    return a


def primes_bit_array(n):
    a = bitarray((n + 1) * bitarray('1'))
    a[0] = 0
    a[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i] == 1:
            for k in range(i + i, n + 1, i):
                a[k] = 0
    return [x for x in range(2, n) if a[x] != 0]


def primes_set(n):
    sie = set(range(2, n + 1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if i in sie:
            sie -= set(range(i * 2, n + 1, i))
    return sie


def primes_list(n):
    sie = list(range(n + 1))
    sie[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if i > 0:
            for k in range(i + i, len(sie), i):
                sie[k] = 0
    return [x for x in sie if x != 0]

if __name__ == "__main__":
    elem = 80000000

    cur = task0.current_milli_time()
    primes_list(elem)
    cur = task0.current_milli_time() - cur
    print(cur)

    cur = task0.current_milli_time()
    primes_set(elem)
    cur = task0.current_milli_time() - cur
    print(cur)

    cur = task0.current_milli_time()
    primes_bit_array(elem)
    cur = task0.current_milli_time() - cur
    print(cur)

    cur = task0.current_milli_time()
    primes_bit_array_2(elem)
    cur = task0.current_milli_time() - cur
    print(cur)
