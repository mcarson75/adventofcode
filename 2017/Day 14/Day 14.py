import numpy as np
from functools import reduce

input = 'ffayrhll'

def hash_array(lengths, iterations):
    pos = 0
    skip = 0
    array = np.array(list(range(256)))

    for i in range(iterations):
        for l in lengths:
            if l <= len(array):
                array = np.roll(array, -pos)
                array[:l] = np.flip(array[:l])
                array = np.roll(array, pos)
                pos += l + skip
                if pos >= len(array):
                    pos -= len(array)
                skip += 1
                
    return array

def get_hex_hash(input):
    chunk = ''
    array = hash_array(input, 64)    
    for n in range(16):
        nibble = reduce(lambda x, y: x ^ y, array[n*16:(n+1)*16])
        chunk += f'{nibble:02x}'
        
    return chunk

def get_on_bits(h): return [True if x=='1' else False for x in list('{:0128b}'.format(int(h, 16)))]

regions = []

def count_regions(x, y, initial=False):
    if y < 0 or y >= len(disk) or x < 0 or x >= len(disk[0]) or not disk[y][x]:
        return
    
    if initial:
        regions.append(0)
    else:
        regions[-1] += 1
        disk[y][x] = False
        
    count_regions(x+1, y)
    count_regions(x-1, y)
    count_regions(x, y+1)
    count_regions(x, y-1)

part1 = 0
disk = np.full((128, 128), False)
for n in range(128):
    string = input + '-' + str(n)
    ascii = [ord(c) for c in list(string)]
    ascii.extend([17, 31, 73, 47, 23])
    hash = get_hex_hash(ascii)
    bits = np.array(get_on_bits(hash))
    part1 += sum(bits)
    disk[n] = bits

for i in range(len(disk)):
    for j in range(len(disk[0])):
        count_regions(j, i, True)

part2 = len(regions)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
