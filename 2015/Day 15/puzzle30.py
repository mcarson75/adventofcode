import numpy as np
from math import prod

matrix = []

#calc = lambda m, weight: prod(max(y, 0) for y in [sum(x) for x in np.multiply(m, weight)])
def calc(m, weight):
    w = np.array(weight)[np.newaxis]
    weighted = np.multiply(m, w.T)
    totals = [max(0, sum(weighted[:,n])) for n in range(len(weighted[0]))]
    calories = totals[-1]
    score = prod(totals[:-1]) if calories == 500 else 0
        
    return score

for line in open("input.txt", 'r', encoding='utf-8'):
    line.strip()
    line = line.replace(',', ' ')
    matrix.append([int(x) for x in line.strip().split()[2::2]])
    
matrix = np.array(matrix)
best = 0

for h in range(100):
    for i in range(100-h):
        for j in range(100-h-i):
            k = 100-h-i-j
            best = max(best, calc(matrix, [h, i, j, k]))

print(best)