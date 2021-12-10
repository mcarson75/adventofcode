import numpy as np

find_min = lambda l: np.r_[True, l[1:] < l[:-1]] & np.r_[l[:-1] < l[1:], True]

with open("input.txt", 'r', encoding='utf-8') as f:
    array = [[ int(s) for s in line.rstrip()] for line in f]
        
array=np.array(array)
checks_row = np.full_like(array, False)
checks_col = np.full_like(array, False)

for row in range(np.size(array, 0)):
    checks_row[row] = find_min(array[row])

for col in range(np.size(array, 1)):
    checks_col[:, col] = find_min(array[:, col])

checks = np.logical_and(checks_row, checks_col)        

heightmap = np.sum(array[np.where(checks==True)]) + np.count_nonzero(checks==True)
print(heightmap)