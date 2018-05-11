import sys
import _io
import re
import math


def count_mean_and_stand_dev(file: _io.TextIOWrapper):
    count = -1
    sum = 0
    squares = 0
    pat = re.compile(r"open .* (\d+) usec")
    for line in file:
        match = pat.match(line)
        if match is not None:
            if count == -1:
                count = 0
                continue
            count += 1
            value = float(match.group(1))
            print(match, match.group(1))
            sum += value
            squares += value ** 2
    mean = sum / count
    return mean, math.sqrt(squares/count - mean ** 2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + __file__ + " file_name")
    else:
        with open(sys.argv[1]) as f:
            print(count_mean_and_stand_dev(f))
