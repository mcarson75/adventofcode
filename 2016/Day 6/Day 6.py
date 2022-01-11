import numpy as np

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
letters = np.array([list(n) for n in lines]).T

part1 = ''
part2 = ''
for l in letters:
    c = sorted(list(l), key=list(l).count, reverse = True)
    part1 += c[0]
    part2 += c[-1]

print("Part 1: " + part1)
print("Part 2: " + part2)