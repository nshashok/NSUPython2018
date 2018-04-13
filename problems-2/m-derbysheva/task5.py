import sys
import codecs

freqs = {
    'о': 0.10983, 'е': 0.08483, 'а': 0.07998, 'и': 0.07367, 'н': 0.06700,
    'т': 0.06318, 'с': 0.05473, 'р': 0.04746, 'в': 0.04533, 'л': 0.04343,
    'к': 0.03486, 'м': 0.03203, 'д': 0.02977, 'п': 0.02804, 'у': 0.02615,
    'я': 0.02001, 'ы': 0.01898, 'ь': 0.01735, 'г': 0.01687, 'з': 0.01641,
    'б': 0.01592, 'ч': 0.01450, 'й': 0.01208, 'х': 0.00966, 'ж': 0.00940,
    'ш': 0.00718, 'ю': 0.00639, 'ц': 0.00486, 'щ': 0.00361, 'э': 0.00331,
    'ф': 0.00267, 'ъ': 0.00037, 'ё': 0.00013
}

encodings = ['koi8-r', 'cp855', 'cp866', 'cp1251',
             'iso_8859-5', 'mac_cyrillic']


def makeTable(file):
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
    return n, check


def encoding_probabilities(filename):
    file = open(filename, 'rb')
    num, table = makeTable(file)

    check = dict.fromkeys(encodings, 0)

    for k in check.keys():
        for key, counter in table.items():
            try:
                char = (bytes([key]).decode(k)).lower()
            except UnicodeDecodeError:
                char = None
            check[k] += abs(counter / num - freqs.get(char, 0))
    return check


try:
    probabilities = encoding_probabilities(sys.argv[1])
    encoding = min(probabilities, key=probabilities.get)

    print('probabilities: ' + str(probabilities))
    if input('open file with ' + encoding + ' encoding? y/n\n') == 'y':
        print(codecs.open(sys.argv[1], encoding=encoding).read())
except Exception as e:
    print(e, file=sys.stderr)
