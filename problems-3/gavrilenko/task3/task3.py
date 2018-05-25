import sys


def file_generator(file):
    end = ""
    if file.mode == "rb":
        end = b""
    for chunk in iter(lambda: file.read(512), end):
        for c in chunk:
            yield c


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        return
    with open(sys.argv[1], "r") as file:
        our_generator = file_generator(file)
        print("HERE WE GO")
        for i in our_generator:
            print(i)
        print("END")


if __name__ == "__main__":
    main()
