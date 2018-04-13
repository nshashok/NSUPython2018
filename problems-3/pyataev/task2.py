#!/usr/bin/python3
import sys, re, math, subprocess

def count(file):
    average = 0
    num = 0
    lines_num = None

    if sys.platform == "linux":
        proc1 = subprocess.Popen(['grep', 'open', file.name], stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(['wc', '-l'], stdin=proc1.stdout, stdout=subprocess.PIPE)
        proc1.stdout.close()
        lines_num = int(proc2.communicate()[0]) - 1
    elif sys.platform == "win32":
        lines_num = int(re.search('(\d+)', str(subprocess.Popen(["find", "/c", "open", file.name], stdout=subprocess.PIPE).stdout.read())).group(0)) - 1 # не проверено

    decil_size = lines_num // 10
    decil_size = decil_size if decil_size != 0 else 1
    decil = [-1] * decil_size # при при предположении, что считываемые числа - значения времени > 0

    for line in file:
        if line.startswith("open"):
            break

    for line in file:
        if not line.startswith('open'):
            continue
        result = re.search('(\d+) usec', line)
        if result:
            value = int(result.group(1))
            average += value
            lmin = min(decil)
            if lmin < value:
                decil.insert(decil.index(lmin), value)
                decil.remove(lmin)
            num += 1

    if num > 0:
        average /= num
    else:
        return None

    return average, min(decil)

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Not enough arguments!")
    else:
        try:
            with open(sys.argv[1], 'r') as f:
                average, decil = count(f)
                print("average : " + str(average) + "\ndecil : " + str(decil))
        except Exception as e:
            print(e.strerror, file=sys.stderr)
