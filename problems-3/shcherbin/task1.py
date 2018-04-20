import sys
import re
import math


def countMeanAndDev(file):
    sum = 0
    sumSquares = 0
    n = 0
    for line in file:
        if line.startswith('open'):
            break
    regex = re.compile(r'(\d+) usec')
    for line in file:
        if line.startswith('open'):
            n += 1
            time = float(re.search(regex, line).group(1))
            sum += time
            sumSquares += time ** 2
    mean = sum / n
    stdDevision = math.sqrt(sumSquares / n - mean ** 2)
    return mean, stdDevision


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter file path")
        filename = input()
    else:
        filename = sys.argv[1]
    with open(filename) as file:
        mean, stdDev = countMeanAndDev(file)
    print("mean time = %f" % mean)
    print("standart devision = %f" % stdDev)
