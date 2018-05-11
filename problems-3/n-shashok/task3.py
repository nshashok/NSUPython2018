import sys

class LazyReader:
    def __init__(self, file):
        self.__f = file
        self.__p = 0
        self.__b_size = 512
        self.__chunk = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.__p == len(self.__chunk):
            self.__chunk = self.__f.read(self.__b_size)
            self.__p = 0
        if self.__chunk is None or len(self.__chunk) == 0:
            raise StopIteration
        next = self.__chunk[self.__p]
        self.__p += 1
        return next


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: " + __file__ + " file_name mode")
    else:
        try:
            with open(sys.argv[1], sys.argv[2]) as f:
                fr = LazyReader(f)
                print(*(i for i in fr), sep="")
        except Exception as e:
            print(e)
