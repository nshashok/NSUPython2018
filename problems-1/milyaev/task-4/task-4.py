import os
import sys


def get_files_list(path):
    if os.path.isdir(path):
        if not os.access(path, os.R_OK):
            raise ValueError("You don't have permission to read this directory.")
    else:
        if not os.access(path, os.F_OK):
            raise ValueError("This directory doesn't exist.")
        else:
            raise ValueError("This is not directory.")

    files = []

    for element in os.listdir(path):
        element_path = os.path.join(path, element)
        if os.path.isfile(element_path):
            statinfo = os.stat(element_path)
            files.append((element, statinfo.st_size))

    return sorted(files, key=lambda x: (-x[1], x[0]))


def main():
    if len(sys.argv) < 2:
        print("Name of directory was not found.")
    else:
        print("path to directory:", sys.argv[1])
        print()
        try:
            file_list = get_files_list(sys.argv[1])
            if not file_list:
                print("This directory doesn't contain any regular files.")
            else:
                for name, size in file_list:
                    print("name:", name + ',', "size:", size)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
