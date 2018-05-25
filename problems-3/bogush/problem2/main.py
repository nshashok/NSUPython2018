#!/usr/local/bin/python3
from heapq import heappush, heappushpop
from math import ceil
from sys import argv

from itertools import islice


def _filtered_lines(file):
    return islice((line for line in file if line.startswith('open')), 1, None)


def _extract_time(line):
    time_str = line[:line.index('usec')].rstrip()
    time_str = time_str[time_str.rindex(' ')+1:]
    return int(time_str)


def process(file):
    count = sum(1 for _ in _filtered_lines(file))
    file.seek(0)
    filtered_lines = _filtered_lines(file)

    heap = []

    first10percent = int(ceil(count * 0.1))

    for line in islice(filtered_lines, 0, first10percent):
        time = _extract_time(line)
        heappush(heap, time)

    for line in filtered_lines:
        time = _extract_time(line)
        heappushpop(heap, time)

    print('upper decile is %d' % heap[0])


def main():
    if len(argv) != 2:
        print("Usage: %s filename" % argv[0])
        exit(1)
    filename = argv[1]
    try:
        with open(filename) as file:
            process(file)
    except Exception as exception:
        print(exception)
        exit(1)
    exit(0)


if __name__ == "__main__":
    main()
