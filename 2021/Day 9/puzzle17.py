import numpy as np

find_min = lambda l: np.r_[True, l[1:] < l[:-1]] & np.r_[l[:-1] < l[1:], True]
column = lambda matrix, i: [row[i] for row in matrix]

array=[]

with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        array.append([int(x) for x in line.rstrip()])
        
array=np.array(array)
checks = np.full_like(array, False)

for row in range(len(array)):
    checks[row] = find_min(array[row])

for col in range(len(array[0])):
    c = np.array(column(array, col))
    c_check = find_min(c)
    for row in range(len(array)):
        r = checks[row]
        checks[row][col] = r[col] and c_check[row]
        
heightmap = np.sum(array[np.where(checks==True)]) + np.count_nonzero(checks==True)
print(heightmap)