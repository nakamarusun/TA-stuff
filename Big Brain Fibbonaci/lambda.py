from functools import reduce
from time import time

fibbonaci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

def fibbonaci_long(n):
    result = [0, 1]
    for i in range(n - 2):
        result += [result[-1] + result[-2]]
    return result

TRIES = 100
start_time = time()
fibbonaci_long(TRIES)
print("fibbonaci classic function: %.20f" % (time() - start_time))

start_time = time()
fibbonaci(TRIES)
print("fibbonaci lambda function: %.20f" % (time() - start_time))