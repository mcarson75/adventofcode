import numpy as np
from collections import defaultdict

get_bin = lambda n, length: np.array([int(x) for x in '{num:0{width}b}'.format(num = n, width = length)])

sizes = np.array([int(x) for x in open('input.txt', 'r', encoding='utf-8')])
    
total = 150
reps = len(sizes)
sol = defaultdict(int)

for n in range(1, 1 << reps):
    bins = get_bin(n, reps)
    t = np.sum(np.multiply(sizes, bins))
    if t == total:
        sol[sum(bins)] += 1

part1 = sum(sol.values())
k = min(sol.keys())
part2 = sol[k]

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))