from matplotlib import pyplot as plt

from timeit import timeit

types = ('list', 'set', 'bitarray')
times = {t: [] for t in types}
numbers = [10**i for i in range(1, 8)]

for t in types:
    print("processing {} n={}...{}".format(t, numbers[0], numbers[-1]))
    for n in numbers:
        setup = "from eratosthenes_{} import primes\nn = {}".format(t, n)
        time = timeit("primes(n)", setup=setup, number=1)
        times[t].append(time)
        print(n, time, sep='\t')

for t in types:
    plt.plot(numbers, times[t], label=t)
plt.xlabel('n')
plt.ylabel('time')
plt.title("Comparison of Eratosthenes sieve using different containers")
plt.legend()
plt.show()
