import heapq
import re
import sys

import math


def count_upper_decile(filename):
    pattern = re.compile(b"(\d+) usec")
    count = 0

    with open(filename, 'rb') as f:
        for line in f:
            if line.startswith(b"open"):
                break

        for line in f:
            if line.startswith(b"open"):
                count += 1

        if count > 0:
            heap_size = int(math.ceil(count / 10))
            heap = [0] * heap_size

            f.seek(0)
            for line in f:
                if line.startswith(b"open"):
                    break

            for line in f:
                if line.startswith(b"open"):
                    value = int(pattern.search(line).group(1))
                    if value > heap[0]:
                        heapq.heappushpop(heap, value)
            return heap[0]
        else:
            return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Name of file was not found.", file=sys.stderr)
    else:
        try:
            upper_decile = count_upper_decile(sys.argv[1])
            if upper_decile is None:
                print("Sample is empty")
            else:
                print("upper decile = {}".format(upper_decile))
        except Exception as e:
            print(e, file=sys.stderr)
