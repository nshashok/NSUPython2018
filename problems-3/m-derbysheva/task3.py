import sys


def reader(file):
    while True:
        data = file.read(512)
        if len(data) == 0:
            break
        for element in data:
            yield element


if len(sys.argv) != 2:
    print("print filename", file=sys.stderr)
    sys.exit(-1)

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        for i in reader(file):
            print(i, end="")

except Exception as e:
    print(e, file=sys.stderr)
