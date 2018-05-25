import sys


class LazyFileReader:

    def __init__(self, file):
        self.file = file
        self.pos = 0
        self.chunck = self.file.read(512)
        self.chunckLen = len(self.chunck)

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == self.chunckLen and self.chunckLen < 512:
            raise StopIteration

        res = self.chunck[self.pos]
        self.pos = (self.pos + 1) % self.chunckLen

        if self.pos == 0:
            self.chunck = self.file.read(512)
            self.chunckLen = len(self.chunck)

        return res


if __name__ == '__main__':
    f = sys.stdin
    for byte in LazyFileReader(f):
        print(byte)
