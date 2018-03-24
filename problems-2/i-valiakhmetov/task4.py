#!/bin/python

import sys

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
	stats_list = sorted(stats.items(), key = lambda k: k[1], reverse=True)
	for k, v in stats_list:
		#print(k.to_bytes(1, byteorder='little').decode('koi8-r'), hex(k), v[1])
		print(hex(k), v[1])
