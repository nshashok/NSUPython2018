import time
import math
from bitarray import bitarray


def eratosthen_list(number) -> list:
    l = list(range(2, number + 1))
    for candidate in range(2,math.ceil(math.sqrt(number))):
        if candidate != 0:
            for cond in range(2 * candidate, number + 1, candidate):
                l[cond - 2] = 0
    return list(filter(lambda x: x != 0, l))


# map + labmda

def eratosthen_set(number) -> set:
    s = set(range(2, number + 1))
    for candidate in range(2,math.ceil(math.sqrt(number))):
        if candidate in s:
            s = s - set(range(2 * candidate, number + 1, candidate))
    return s


def eratosthen_bitarray(number):
    arr = bitarray(number + 1)
    arr.setall(True)
    arr[0] = False
    arr[1] = False
    for i in range(math.ceil(math.sqrt(number))):
        if not arr[i]:
            continue
        for j in range(2 * i, number + 1, i):
            arr[j] = False
    return arr


if __name__ == '__main__':
    l_start = time.time()
    l = eratosthen_list(100000000)
    l_time = time.time() - l_start
    s_start = time.time()
    s = eratosthen_set(100000000)
    s_time = time.time() - s_start
    print(l)
    print(l_time)
    print(s)
    print(s_time)
    a_start = time.time()
    a = eratosthen_bitarray(100000000)
    a_time = time.time() - a_start
    print(a)
    print(a_time)