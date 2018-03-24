#!/bin/python

import sys
import codecs
from difflib import SequenceMatcher

#https://www.dpva.ru/Guide/GuideUnitsAlphabets/Alphabets/FrequencyRuLetters/
alphabet = "оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё"
cyr_enc = ['koi8_r','cp1251', 'iso8859_5', 'cp855', 'cp866', 'mac_cyrillic']

def guess_encoding(stats):
	stats_sorted = sorted(stats.items(), key = lambda k: k[1], reverse=True)
	br = bytearray()
	a = []

	for k, v in stats_sorted:
		br.extend(k.to_bytes(1, byteorder='little'))

	for enc in cyr_enc:
		try:
			dec = br.decode(enc)
			a.append([enc, SequenceMatcher(None, alphabet, dec).ratio()])
		except UnicodeDecodeError:
			pass
	return sorted(a, key = lambda k: k[1], reverse=True)

def get_freq(filename):
	stats = {}
	n = 0

	with open(filename, "rb") as f:
		byte = f.read(1)
		while byte:
			a = int.from_bytes(byte, 'little')
			if (a > 127):
				if a in stats:
					stats[a][0] += 1
				else:
					stats[a] = [1, 0]
				n += 1
			byte = f.read(1)

	for k, v in stats.items():
		v[1] = v[0]*(100/n)

	return stats

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Usage: %s filename' % sys.argv[0])

	stats = get_freq(sys.argv[1])
	matches = guess_encoding(stats)

	print("Best match:", matches[0][0], matches[0][1], "\n")
	for k, v in matches[1:-1]:
		print(k, v)
	print("\nUsing", matches[0][0],"to read", sys.argv[1], "...\n")

	with codecs.open(sys.argv[1], encoding=matches[0][0]) as f:
		line = f.readline()
		while line:
			print(line.strip())
			line = f.readline()
