import numpy as np
from functools import reduce

input = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
lengths = [int(x) for x in input[0].split(',')]

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

part1_array = hash_array(lengths, 1)
part1 = np.prod(part1_array[:2])

ascii_lengths = []
for c in input[0]:
    ascii_lengths.append(ord(c))
    
ascii_lengths.extend([17, 31, 73, 47, 23])
part2_array = hash_array(ascii_lengths, 64)
part2 = ''

for n in range(16):
    chunk = reduce(lambda x, y: x ^ y, part2_array[n*16:(n+1)*16])
    part2 += f'{chunk:02x}'

print("Part 1: " + str(part1))
print("Part 2: " + part2)