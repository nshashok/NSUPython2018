#!/bin/python3

import sys
import re
import math
import heapq

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Usage: %s filename' % sys.argv[0])

	n = 0
	sum = 0
	regex = re.compile("open .* (\d+) usec")
	with open(sys.argv[1], "r") as f:
		for line in f:
			m = regex.match(line)
			if m is not None:
				elem = int(m.group(1))
				sum += elem
				n += 1
		mean = sum / n

		f.seek(0)
		heap_size = math.ceil(n*0.1)
		heap = []
		n = 0
		for line in f:
			m = regex.match(line)
			if m is not None:
				elem = int(m.group(1))
				heap.append(elem)
				if (heap_size < n):
					break
				n += 1

		heapq.heapify(heap)
		decile = 0
		for line in f:
			m = regex.match(line)
			if m is not None:
				elem = int(m.group(1))
				if (heap[0] < elem):
					decile = heapq.heapreplace(heap, elem)

		print("mean:", mean)
		print("decile:", decile)
