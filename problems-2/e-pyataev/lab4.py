#!/usr/bin/python3
import sys

def count_freqs(file):
    freqs = {}
    value = 127
    count = 0

    while True:
        n = file.read(256)
        if not n:
            break
        for i in n:
            if(i > 127):
                freqs[i] = freqs.get(i, 0) + 1
                count += 1
    if count > 0:
        for k in freqs.keys():
            freqs[k] = freqs[k] / count * 100

    return freqs

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Not enough arguments!")
    else:
        try:
            with open(sys.argv[1], 'rb') as f:
                frequences = count_freqs(f)
                for a, b in sorted(frequences.items(), key=lambda x: x[1]):
                    print(bytes([a]), " ", b)
        except Exception as e:
            print(e.strerror, file=sys.stderr)
