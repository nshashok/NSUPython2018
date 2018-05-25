import sys
import os


def get_file_stat(filename):
    dict = {i: 0 for i in range(128, 256)}
    count = 0

    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(256), b""):
            for i in chunk:
                if i > 127:
                    dict[i] += 1
                    count += 1
    if count != 0:
        for i in dict:
            dict[i] = dict[i] * 100 / count

    return sorted(dict.items(), key=lambda x: x[1], reverse=True)


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        return

    try:
        print(os.linesep.join(str(i) for i in get_file_stat(sys.argv[1]) if i[1] != 0))

    except OSError as e:
        print("We got a problem")
        print(e)


if __name__ == "__main__":
    main()
