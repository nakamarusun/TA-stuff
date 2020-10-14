from functools import reduce

fibbonaci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

def fibbonaci_long(n):
    result = [0, 1]
    for i in range(n - 2):
        result += [result[-1] + result[-2]]
    return result

print(fibbonaci_long(10))
print(fibbonaci(10))