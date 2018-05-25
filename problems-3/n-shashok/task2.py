import _io
import re
import heapq
import sys
import math


def count_decil(file: _io.TextIOWrapper):
    n = math.ceil(0.1 * sum(1 for l in file if l.startswith("open")))
    file.seek(0)
    dec = [0] * n
    pat = re.compile(r"open .* (\d+) usec")
    for l in file:
        match = pat.match(l)
        if match is not None:
            value = float(match.group(1))
            if value > dec[0]:
                heapq.heappushpop(dec, value)
    return dec[0]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + __file__ + " file_name")
    else:
        with open(sys.argv[1]) as f:
            print("Decil:", count_decil(f))
