#!/usr/bin/python3
import os, sys

def print_files(path):
    try:
        l = [[x, y] for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) for y in [os.stat(os.path.join(path, x)).st_size]]
        l.sort(key=lambda x: (-x[1], x[0]))

        for k, v in l:
            print(k, v)

    except Exception as e:
        print(e, file=sys.stderr)

if(len(sys.argv) > 1):
    print_files(sys.argv[1])
