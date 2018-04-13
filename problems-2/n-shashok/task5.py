import task4
import sys


encodings = ("cp855", "cp866", "cp1251", "iso8859_5", "koi8-r", "mac_cyrillic")

frequency = {
    "о": 10.983,
    "е": 8.483,
    "а": 7.998,
    "и": 7.367,
    "н": 6.7,
    "т": 6.318,
    "с": 5.473,
    "р": 4.746,
    "в": 4.533,
    "л": 4.343,
    "к": 3.486,
    "м": 3.203,
    "д": 2.977,
    "п": 2.804,
    "у": 2.615,
    "я": 2.001,
    "ы": 1.898,
    "ь": 1.735,
    "г": 1.687,
    "з": 1.687,
    "б": 1.592,
    "ч": 1.45,
    "й": 1.208,
    "х": 0.966,
    "ж": 0.94,
    "ш": 0.718,
    "ю": 0.638,
    "ц": 0.486,
    "щ": 0.361,
    "э": 0.331,
    "ф": 0.267,
    "ъ": 0.037,
    "ё": 0.013
}


def detect_encoding(filename):
    bytes_freq = task4.get_bytes(filename)
    print(bytes_freq)
    encodings_coefficients = {}
    for item in bytes_freq:
        for encoding in encodings:
            print(encoding)
            try:
                print(item[0].decode(encoding), (item[0].decode(encoding)).lower(), (item[0].decode(encoding)).lower())
                encodings_coefficients[encoding] = \
                    encodings_coefficients.get(encoding, 0) - \
                    abs(frequency[(item[0].decode(encoding)).lower()] - item[1])
            except KeyError:
                encodings_coefficients[encoding] = \
                    encodings_coefficients.get(encoding, 0)# + item[1]
        print()
    print(encodings_coefficients)
    return min(encodings_coefficients, key=encodings_coefficients.get)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + __file__ + " file_name")
    else:
        try:
            enc = str(detect_encoding(sys.argv[1]))
            with open(sys.argv[1], "rb") as f:
                for line in f:
                    print(line.decode(enc))
            print("Encoding: ", enc)

        except OSError as e:
            print("Unable to read: ", e, file=sys.stderr)
