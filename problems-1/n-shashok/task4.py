import os
import sys


def sorted_files(directory):
    try:
        files = [os.path.join(os.path.abspath(directory), f)
             for f in os.listdir(os.path.abspath(directory))
             if os.path.isfile(os.path.join(os.path.abspath(directory), f))]
        files.sort(key=lambda x: (os.stat(x).st_size, x.lower()))
        for file in files:
            print(file)
    except OSError as e:
        print("Unable to read: ", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + __file__ + " dirname")
    else:
        sorted_files(sys.argv[1])
