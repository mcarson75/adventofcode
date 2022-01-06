import numpy as np
from math import prod

matrix = []

def calc(m, weight):
    w = np.array(weight)[np.newaxis]
    weighted = np.multiply(m, w.T)

    totals = np.sum(weighted, axis = 0)
    totals = np.where(totals < 0, 0, totals)
    
    score = prod(totals[:-1])
    calories = totals[-1]
    
    return score, calories == 500

for line in open("input.txt", 'r', encoding='utf-8'):
    line.strip()
    line = line.replace(',', ' ')
    matrix.append([int(x) for x in line.strip().split()[2::2]])
    
matrix = np.array(matrix)
part1 = 0
part2 = 0

for h in range(100):
    for i in range(100-h):
        for j in range(100-h-i):
            k = 100-h-i-j
            score, cal = calc(matrix, [h, i, j, k])
            part1 = max(score, part1)
            if cal:
                part2 = max(score, part2)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))