import numpy as np

with open("input.txt", 'r', encoding='utf-8') as f:
    pos = np.array([int(x) for x in f.read().rstrip().split(",")])

min_fuel = int(np.sum(np.abs(np.add(pos, -1*np.median(pos)))))
        
print(min_fuel)