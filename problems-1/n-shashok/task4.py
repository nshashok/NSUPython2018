import os
import sys


def sorted_files(directory):
    files = [os.path.join(os.path.abspath(directory), f)
         for f in os.listdir(os.path.abspath(directory))
         if os.path.isfile(os.path.join(os.path.abspath(directory), f))]
    files.sort(key=lambda x: (os.stat(x).st_size, x.lower()))
    for file in files:
        print(file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + __file__ + " dirname")
    else:
        try:
            sorted_files(sys.argv[1])
        except OSError as e:
            print("Unable to read: ", e, file=sys.stderr)
