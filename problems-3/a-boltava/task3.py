class BufferedReader:

    def __init__(self, file):
        self.__source = file
        self.__buffer = []
        self.__position = 0
        self.__max_buffer_size = 512

    def __iter__(self):
        return self

    def __next__(self):
        if self.__position == len(self.__buffer):
            self.__buffer = self.__source.read(self.__max_buffer_size)
            self.__position = 0

        if len(self.__buffer) == 0:
            raise StopIteration()

        result = self.__buffer[self.__position]
        self.__position += 1
        return result
