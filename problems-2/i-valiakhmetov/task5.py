#!/bin/python
#This file is encoded in utf-8

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
		br.extend(k.to_bytes(1, 'little'))

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

	with open(filename, "rb", 8192) as f:
		bytes = f.read(1024)
		while bytes:
			for byte in bytes:
				if (byte > 127):
					if byte in stats:
						stats[byte][0] += 1
					else:
						stats[byte] = [1, 0]
					n += 1
			bytes = f.read(1024)

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
