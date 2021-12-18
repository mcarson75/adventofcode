from hashlib import md5
import random

input = 'wtnhxymk'

pw = [None] * 8
num = 0
while any([i == None for i in pw]):
    m = md5(str.encode(input + str(num))).hexdigest()
    if m[:5] == '00000':
        pos = int(m[5], 16) 
        if pos < 8 and pw[pos] == None:
            pw[pos] = m[6]
    if num % 30000 == 0:
        s = [c if c else str(random.randint(0, 9)) for c in pw]
        print(''.join(s) + '\r', end='')
    num += 1
    
print(''.join(pw))