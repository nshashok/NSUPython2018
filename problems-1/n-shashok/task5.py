import math
import task2
import task0


def primes_list_1(n):
    return [x for x in range(2, n + 1) if x not in
            [element for sublist in
            [list(range(2 * j, n + 1, j)) for j in range(2, int(math.sqrt(n)) + 1)]
            for element in sublist]]


def primes_list_2(n):
    return [x for x in range(2, n + 1) if task2.is_prime(x)]


if __name__ == "__main__":
    elem = 10000

    cur = task0.current_milli_time()
    primes_list_1(elem)
    cur = task0.current_milli_time() - cur
    print(cur)

    cur = task0.current_milli_time()
    primes_list_2(elem)
    cur = task0.current_milli_time() - cur
    print(cur)