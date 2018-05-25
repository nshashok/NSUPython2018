#!/usr/bin/python3
import sys

def gen_read(file):
    mode = '' if file.mode == 'r' else b''
    for buf in iter(lambda: file.read(512), mode):
        for val in buf:
            yield val

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Not enough arguments!")
    else:
        try:
            with open(sys.argv[1], 'r') as f:
                gen = gen_read(f)
                for val in gen:
                    print(val, end="")
        except Exception as e:
            print(val)
            print(e.strerror, file=sys.stderr)
