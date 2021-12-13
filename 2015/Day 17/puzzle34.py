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
num_bins = np.array([])

for n in range(2**reps):
    bins = get_bin(n, reps)
    t = np.sum(np.multiply(sizes, bins))
    if t == total: num_bins = np.append(num_bins, sum(bins))
    
num = np.count_nonzero(np.where(num_bins==np.min(num_bins)))

print(num)