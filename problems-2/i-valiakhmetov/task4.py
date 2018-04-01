#!/bin/python3

import sys

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
	stats_list = sorted(stats.items(), key = lambda k: k[1], reverse=True)
	for k, v in stats_list:
		#print(k.to_bytes(1, byteorder='little').decode('koi8-r'), hex(k), v[1])
		print(hex(k), v[1])
