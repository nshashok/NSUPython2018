import task4
import sys


encodings = ("cp855", "cp866", "cp1251", "iso8859_5", "koi8_r", "mac_cyrillic")

ru_freqs = {
    'о': 0.10983, 'е': 0.08483, 'а': 0.07998, 'и': 0.07367, 'н': 0.06700,
    'т': 0.06318, 'с': 0.05473, 'р': 0.04746, 'в': 0.04533, 'л': 0.04343,
    'к': 0.03486, 'м': 0.03203, 'д': 0.02977, 'п': 0.02804, 'у': 0.02615,
    'я': 0.02001, 'ы': 0.01898, 'ь': 0.01735, 'г': 0.01687, 'з': 0.01641,
    'б': 0.01592, 'ч': 0.01450, 'й': 0.01208, 'х': 0.00966, 'ж': 0.00940,
    'ш': 0.00718, 'ю': 0.00639, 'ц': 0.00486, 'щ': 0.00361, 'э': 0.00331,
    'ф': 0.00267, 'ъ': 0.00037, 'ё': 0.00013
}


def get_closest_encoding(freq_tuple):
    encodings_err = {encoding: 0 for encoding in encodings}

    for encoding in encodings:
        for byte, freq in freq_tuple:
            try:
                char = bytes([byte]).decode(encoding).lower()
                encodings_err[encoding] += abs(ru_freqs[char] - freq / 100)
            except (UnicodeDecodeError, KeyError):
                pass

    return min(encodings_err, key=encodings_err.get)


def main():
    if len(sys.argv) != 2:
        print("Wrong arguments")
        return
    try:
        print(get_closest_encoding(task4.get_file_stat(sys.argv[1])))
    except OSError:
        print("Can't read the file")
        return


if __name__ == "__main__":
    main()
