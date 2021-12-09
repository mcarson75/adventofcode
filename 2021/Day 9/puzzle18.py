from math import prod

with open("input.txt", 'r', encoding='utf-8') as f:
    is_basin = [[ int(s) < 9 for s in line.rstrip()] for line in f]

basins = []

def count_basins(x, y, initial=False):
    if y < 0 or y >= len(is_basin) or x < 0 or x >= len(is_basin[0]) or not is_basin[y][x]:
        return
    
    if initial:
        basins.append(0)
    else:
        basins[-1] += 1
        is_basin[y][x] = False
        
    count_basins(x+1, y)
    count_basins(x-1, y)
    count_basins(x, y+1)
    count_basins(x, y-1)

for i in range(len(is_basin)):
    for j in range(len(is_basin[0])):
        count_basins(j, i, True)
        
basins.sort(reverse=True)

print(prod(basins[:3]))