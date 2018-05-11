import re
import sys

import math


def count_mean_and_std_deviation(filename):
    pattern = re.compile(b"(\d+) usec")
    count = 0
    sum = 0
    sum_squares = 0

    with open(filename, 'rb') as f:
        for line in f:
            if line.startswith(b"open"):
                break

        for line in f:
            if line.startswith(b"open"):
                value = int(pattern.search(line).group(1))
                count += 1
                sum += value
                sum_squares += value * value

        if count > 0:
            mean = sum / count
            deviation = math.sqrt(sum_squares / count - mean ** 2)
            return mean, deviation
        else:
            return None, None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Name of file was not found.", file=sys.stderr)
    else:
        try:
            mean, deviation = count_mean_and_std_deviation(sys.argv[1])
            if mean is None:
                print("Sample is empty")
            else:
                print("Mean = {}".format(mean))
                print("Standard deviation = {}".format(deviation))
        except Exception as e:
            print(e, file=sys.stderr)
