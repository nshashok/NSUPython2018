import sys
from typing import Dict


def print_err(*values, sep=' ', end='\n'):
    print(*values, sep=sep, end=end, file=sys.stderr)


def count_bytes_frequencies(byte_stream) -> Dict[int, float]:
    frequencies = {}
    border_byte = 127
    non_ascii_bytes_count = 0
    reading_chunk = 1024

    def count_bytes(bytes_array) -> int:
        counter = 0
        for byte in bytes_array:
            if byte > border_byte:
                frequencies[byte] = frequencies.get(byte, 0) + 1
                counter += 1
        return counter

    while True:
        input_bytes = byte_stream.read(reading_chunk)
        if not input_bytes: break
        non_ascii_bytes_count += count_bytes(input_bytes)

    if non_ascii_bytes_count > 0:
        for key in frequencies.keys():
            frequencies[key] = frequencies[key] / non_ascii_bytes_count

    return frequencies


def pretty_print_frequencies(frequencies: Dict[int, float]) -> None:
    if len(frequencies) == 0: return

    sorted_keys = sorted(frequencies.keys(), key=frequencies.get, reverse=True)
    header = "Byte -- Frequency"
    print("-" * len(header))
    print("Number of unique bytes: {}".format(len(frequencies)))
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for key in sorted_keys:
        print("{0} --- {1:.6}".format(key, 100*frequencies[key]))


def print_help(program_name):
    print("Usage: python3 {} path".format(program_name))
    print("path - path to file, which should be processed")


def main(argv):
    file_path = argv[1]
    try:
        with open(file=file_path, mode="rb") as file:
            bytes_frequencies = count_bytes_frequencies(file)
            pretty_print_frequencies(bytes_frequencies)
    except IOError as e:
        print("Failed to open file {}: {}".format(file_path, e))
    except Exception as e:
        print("Unknown error")
        print_err(e)


if __name__ == "__main__":
    MIN_ARGS_COUNT = 2
    if len(sys.argv) < MIN_ARGS_COUNT:
        print_help(sys.argv[0])
    else:
        main(sys.argv)
