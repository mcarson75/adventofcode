from hashlib import md5
import random

input = 'wtnhxymk'

part1 = ''
num = 0
while len(part1) < 8:
    m = md5(str.encode(input + str(num))).hexdigest()
    if m[:5] == '00000':
        part1 += m[5]
    num += 1
    
print("Part 1: " + part1)

part2 = [None] * 8
num = 0
while any([i == None for i in part2]):
    m = md5(str.encode(input + str(num))).hexdigest()
    if m[:5] == '00000':
        pos = int(m[5], 16) 
        if pos < 8 and part2[pos] == None:
            part2[pos] = m[6]
    if num % 30000 == 0:
        s = [c if c else str(random.randint(0, 9)) for c in part2]
        print("Part 2: " + ''.join(s) + '\r', end='')
    num += 1
    
print("Part 2: " + ''.join(part2))