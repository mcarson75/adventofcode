import numpy as np
from math import prod

matrix = []

def calc(m, weight):
    w = np.array(weight)[np.newaxis]
    weighted = np.multiply(m, w.T)
    return prod([max(0, sum(weighted[:,n])) for n in range(len(weighted[0]))])

for line in open("input.txt", 'r', encoding='utf-8'):
    line.strip()
    line = line.replace(',', ' ')
    matrix.append([int(x) for x in line.strip().split()[2:9:2]])
    
matrix = np.array(matrix)
best = 0

for h in range(100):
    for i in range(100-h):
        for j in range(100-h-i):
            k = 100-h-i-j
            best = max(best, calc(matrix, [h, i, j, k]))

print(best)