#!/usr/bin/python3
import sys, re, math

def count(file):
    average = 0
    deviation = 0
    num = 0

    for line in file:
        if line.startswith("open"):
            break
    for line in file:
        result = re.search('(\d+) usec', line)
        if result:
            value = int(result.group(1))
            average += value
            deviation += value * value
            num += 1
    if num > 0:
        average /= num
        deviation = math.sqrt(deviation / num)
    else:
        return None

    return average, deviation

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Not enough arguments!")
    else:
        try:
            with open(sys.argv[1], 'r') as f:
                average, deviation = count(f)
                print("average : " + str(average) + "\ndeviation : " + str(deviation))
        except Exception as e:
            print(e.strerror, file=sys.stderr)
