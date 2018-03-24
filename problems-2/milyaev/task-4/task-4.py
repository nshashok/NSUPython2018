import sys


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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Name of file was not found.", file=sys.stderr)
    else:
        try:
            freq_dict = count_frequency(sys.argv[1])
            if not freq_dict:
                print("This file doesn't contains non-ascii symbols:", sys.argv[1])
            else:
                for key, value in sorted(freq_dict.items(), key=lambda x: (-x[1], x[0])):
                    # print("{} - {:.4f}".format(bytes([key]).decode('koi8_r'), value))
                    print("{} - {:.4f}".format(key, value))
        except Exception as e:
            print(e, file=sys.stderr)
