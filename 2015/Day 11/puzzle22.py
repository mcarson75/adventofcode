from numpy import diff
from itertools import groupby

input = 'cqjxxzaa'
bad_chars = ['i', 'o', 'l']

next_alpha = lambda s: chr((ord(s)+1 - 97) % 26 + 97)
check_bad_chars = lambda s: not any([c in s for c in bad_chars])

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
    return ''.join(t)
    
while not check_bad_chars(input) or not check_pairs(input) or not check_increasing(input):
    for i in range(-1,-len(input),-1):
        input = inc_char(input, i)
        if not input[i] == 'a':
            break
        
print(input)