import os
import sys


def get_files_list(path):
    if not os.path.isdir(path):
        raise ValueError(path + ": is not directory")

    files = {}

    for element in os.listdir(path):
        element_path = os.path.join(path, element)
        if os.path.isfile(element_path):
            statinfo = os.stat(element_path)
            files[element] = statinfo.st_size

    return sorted(files.items(), key=lambda item: item[1], reverse=True)


def main():
    if len(sys.argv) < 2:
        raise ValueError("Name of directory was not found")

    print(*get_files_list(sys.argv[1]), sep='\n')


if __name__ == "__main__":
    main()
