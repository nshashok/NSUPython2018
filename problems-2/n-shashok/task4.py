import sys
import operator


def get_bytes(filename):
    lang = {}
    count = 0
    with open(filename, "rb") as f:
        byte = f.read(1)
        while byte != b'':
            if bytearray(byte)[0] > 127:
                count += 1
                lang[byte] = lang.get(byte, 0) + 1
            byte = f.read(1)
    to_ret = {n: (lang[n] * 100 / count) for n in list(lang.keys())}
    return sorted(to_ret.items(), key=operator.itemgetter(1), reverse=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + __file__ + " directory_name")
    else:
        try:
            print(get_bytes(sys.argv[1]))
        except OSError as e:
            print("Unable to read: ", e, file=sys.stderr)
