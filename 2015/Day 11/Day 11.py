from numpy import diff
from itertools import groupby

input = 'cqjxjnds'
bad_chars = ['i', 'o', 'l']

next_alpha = lambda s: chr((ord(s)+1 - 97) % 26 + 97)

def check_pairs(s):
    o = [1 if x==y else 0 for x, y in zip(s[1:], s[:-1])]
    t = groupby(o)
    
    return len([x for x, y in t if x==1]) > 1    

def check_increasing(s):
    o = diff([ord(a) for a in s])
    p = ''.join(['1' if i == 1 else '0' for i in o ])

    return '11' in p

def inc_char(s, i):
    t = list(s)
    t[i] = next_alpha(t[i])
    if t[i] in bad_chars:
        t[i] = next_alpha(t[i])
    return ''.join(t)

def inc_string(s):
    for i in range(-1,-len(s),-1):
        s = inc_char(s, i)
        if not s[i] == 'a':
            break
    return s

for n in range(2):    
    while not check_pairs(input) or not check_increasing(input):
        input = inc_string(input)
    if n == 0: part1 = input
    if n == 1: part2 = input
    input = inc_string(input)
        
print("Part 1: " + part1)
print("Part 2: " + part2)