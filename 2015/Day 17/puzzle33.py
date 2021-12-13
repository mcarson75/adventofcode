import numpy as np

def get_bin(n, length):
    arr = []
    for i in range(length-1, -1, -1):
        arr.append((n & 1<<i)>>i)
    return np.array(arr)

with open('input.txt', 'r', encoding='utf-8') as f:
    sizes = np.array([int(x) for x in f])
    
total = 150
reps = len(sizes)
valid = 0

for n in range(2**reps):
    t = np.sum(np.multiply(sizes, get_bin(n, reps)))
    if t == total: valid += 1
    
print(valid)