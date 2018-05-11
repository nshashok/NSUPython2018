import sys


class BufferedReader:
    def __init__(self, file):
        self.__file = file
        self.__buffer = []
        self.__position = 0
        self.__buffer_size = 512

    def __iter__(self):
        return self

    def __next__(self):
        if self.__position == len(self.__buffer):
            self.__buffer = self.__file.read(self.__buffer_size)
            self.__position = 0
        if len(self.__buffer) == 0:
            raise StopIteration
        elem = self.__buffer[self.__position]
        self.__position += 1
        return elem


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Name of file was not found.", file=sys.stderr)
    else:
        try:
            with open(sys.argv[1], "r") as f:
                for elem in BufferedReader(f):
                    if f.mode == "rb":
                        print(elem)
                    elif f.mode == "r":
                        print(elem, end="")
        except Exception as e:
            print(e, file=sys.stderr)
