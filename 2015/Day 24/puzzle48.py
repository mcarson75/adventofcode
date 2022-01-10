from itertools import combinations
from math import prod

pkg = [int(l.strip()) for l in open("input.txt", 'r', encoding='utf-8').readlines()]

parts = 4
size_per = sum(pkg) // parts

def hasSum(lst, sub):
    for y in range(1, len(lst)):
        for x in (z for z in combinations(lst, y) if sum(z) == size_per):
            if sub == 2:
                return True
            elif sub < parts:
                return hasSum(list(set(lst) - set(x)), sub - 1)
            elif hasSum(list(set(lst) - set(x)), sub - 1):
                return prod(x)

print(hasSum(pkg, parts))