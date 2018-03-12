import os
import sys


def get_files_list(path):
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
        try:
            file_list = get_files_list(sys.argv[1])
            if not file_list:
                print("This directory doesn't contain any regular files:", sys.argv[1])
            else:
                for name, size in file_list:
                    print("name:", name + ',', "size:", size)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
