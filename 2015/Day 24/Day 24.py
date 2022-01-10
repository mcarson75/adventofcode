from itertools import combinations
from math import prod

pkg = [int(l.strip()) for l in open("input.txt", 'r', encoding='utf-8').readlines()]


def hasSum(lst, sub, parts):
    size_per = sum(lst) // parts
    for y in range(1, len(lst)):
        for x in (z for z in combinations(lst, y) if sum(z) == size_per):
            if sub == 2:
                return True
            elif sub < parts:
                return hasSum(list(set(lst) - set(x)), sub - 1, parts)
            elif hasSum(list(set(lst) - set(x)), sub - 1, parts):
                return prod(x)

part1 = hasSum(pkg, 3, 3)
part2 = hasSum(pkg, 4, 4)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
