import sys
import operator
import binascii


def get_bytes(filename):
    lang = {}
    count = 0
    with open(filename, "rb") as f:
        bytes_read = f.read(512)
        while True:
            if not bytes_read:
                break
            bytes_read = f.read(512)
            for byte in bytes_read:
                if byte > 127:
                    count += 1
                    cha = bytearray([byte])
                    lang[bytes(cha)] = lang.get(bytes(cha), 0) + 1
    to_ret = {n: (lang[n] * 100 / count) for n in list(lang.keys())}
    return sorted(to_ret.items(), key=operator.itemgetter(1), reverse=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + __file__ + " file_name")
    else:
        try:
            print(get_bytes(sys.argv[1]))
        except OSError as e:
            print("Unable to read: ", e, file=sys.stderr)
