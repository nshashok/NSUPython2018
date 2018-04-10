#!/usr/local/bin/python3
from sys import argv

from math import sqrt


def process(file):
    filtered_lines = (line for line in iter(file.readline, '') if line.startswith('open'))
    filtered_lines = iter(filtered_lines)
    next(filtered_lines) # skip first
    sum = 0.0
    sum_squares = 0.0
    count = 0
    for line in filtered_lines:
        time_str = line[:line.index('usec')].rstrip()
        time_str = time_str[time_str.rindex(' ')+1:]
        time = int(time_str)
        count += 1
        sum += time
        sum_squares += time ** 2
    print('count = %d' % count)
    mean = sum / count
    print('mean = %.2f' % mean)
    std_dev = sqrt((sum_squares - 2 * sum * mean + count * mean ** 2) / (count - 1))
    print('std_dev = %.2f' % std_dev)


def main():
    if len(argv) != 2:
        print("Usage: %s filename" % argv[0])
        exit(1)
    filename = argv[1]
    try:
        with open(filename) as file:
            process(file)
    except FileNotFoundError as err:
        print(err)
        exit(1)
    except Exception as exception:
        print(exception)
        exit(1)
    exit(0)


if __name__ == "__main__":
    main()
