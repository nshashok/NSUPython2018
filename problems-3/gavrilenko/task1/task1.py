import sys


def calculate_open_time(filename):
    with open(filename, "r") as file:
        open_lines = (line for line in iter(file.readline, "") if line.startswith("open"))
        iterator = iter(open_lines)
        next(iterator)

        sum = sqr_sum = n = 0
        for line in iterator:
            usec = int(line.split(" ")[2])
            sum += usec
            sqr_sum += usec ** 2
            n += 1
        if n != 0:
            x = sum / n
            return x, (sqr_sum / n - x ** 2) ** (1/2)


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        return
    try:
        values = calculate_open_time(sys.argv[1])
        print("Average = {} Dispersion = {}".format(values[0], values[1]))

    except OSError as e:
        print("Some trouble with file")
        print(e)
    except StopIteration as e:
        print("File is bad")
        print(e)


if __name__ == "__main__":
    main()
