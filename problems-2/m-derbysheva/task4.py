import sys

try:
    file = open(sys.argv[1], 'rb')
    n = 0

    check = dict.fromkeys(range(128, 256), 0)
    while True:
        data = file.read(1024)
        if len(data) == 0:
            break
        for i in data:
            if i > 127:
                check[i] += 1
                n += 1

    for key, counter in sorted(check.items(),
                               key=lambda element: element[1], reverse=True):
        if counter > 0:
            char = bytes([key]).decode('cp1251')
            print(char + " " + str(counter / n))

except IndexError as e:
    print(e, file=sys.stderr)
