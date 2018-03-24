import sys
import codecs

from math import sqrt

frequencies = {
    'о': 0.10983, 'е': 0.08483, 'а': 0.07998, 'и': 0.07367, 'н': 0.06700,
    'т': 0.06318, 'с': 0.05473, 'р': 0.04746, 'в': 0.04533, 'л': 0.04343,
    'к': 0.03486, 'м': 0.03203, 'д': 0.02977, 'п': 0.02804, 'у': 0.02615,
    'я': 0.02001, 'ы': 0.01898, 'ь': 0.01735, 'г': 0.01687, 'з': 0.01641,
    'б': 0.01592, 'ч': 0.01450, 'й': 0.01208, 'х': 0.00966, 'ж': 0.00940,
    'ш': 0.00718, 'ю': 0.00639, 'ц': 0.00486, 'щ': 0.00361, 'э': 0.00331,
    'ф': 0.00267, 'ъ': 0.00037, 'ё': 0.00013
}

encodings = ['cp855', 'cp866', 'cp1251', 'iso8859_5', 'koi8_r', 'mac_cyrillic']


def count_frequency(filename):
    freq = {}
    number = 0
    chunk_size = 1024

    with open(filename, 'rb') as f:
        while True:
            bytes_chunk = f.read(chunk_size)
            if not bytes_chunk:
                break
            for byte in bytes_chunk:
                if byte > 127:
                    freq[byte] = freq.get(byte, 0) + 1
                    number += 1

    if number > 0:
        for key in freq.keys():
            freq[key] /= number

    return freq


def count_distance(frequency_dict):
    encodings_distances = dict.fromkeys(encodings, 0)

    for i in encodings_distances:
        for key, freq in frequency_dict.items():
            symbol = bytes([key]).decode(i).lower()
            encodings_distances[i] += (freq - frequencies.get(symbol, 0)) ** 2
        encodings_distances[i] = sqrt(encodings_distances[i])

    return encodings_distances


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Name of file was not found.", file=sys.stderr)
    else:
        try:
            freq_dict = count_frequency(sys.argv[1])
            if not freq_dict:
                print("This file doesn't contains non-ascii symbols:", sys.argv[1])
            else:
                distances = count_distance(freq_dict)
                predicted_encoding = min(distances.items(), key=lambda x: x[1])[0]
                print("Predicted encoding:", predicted_encoding)
                print(codecs.open(sys.argv[1], encoding=predicted_encoding).read())
        except Exception as e:
            print(e, file=sys.stderr)
