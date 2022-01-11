import re

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

def check_abba(nib): return nib[0] == nib[3] and nib[1] == nib[2] and nib[0] != nib[1]
def check_aba(nib): return nib[0] == nib[2] and nib[0] != nib[1]
def reverse_nib(nib): return ''.join([nib[1], nib[0], nib[1]]) if check_aba(nib) else ''

def check_pattern(s, type):
    nibs = [s[i:i + len(type)] for i in range(0, len(s) - len(type) + 1)]
    if type == 'abba':
        func = check_abba
    elif type == 'aba':
        func = check_aba
    return [n for n in nibs if func(n)]

part1 = 0
part2 = 0
for l in lines:
    m = re.split(r'\[|\]', l)
    
    if any([check_pattern(a, 'abba') for a in m[::2]]) and not any([check_pattern(a, 'abba') for a in m[1::2]]):
        part1 += 1
        
    aba = [item for sublist in [check_pattern(a, 'aba') for a in m[::2]] for item in sublist]
    bab = [item for sublist in [check_pattern(a, 'aba') for a in m[1::2]] for item in sublist]
    for a, b in [(x, y) for x in aba for y in bab]:
        if b == reverse_nib(a):
            part2 += 1
            break
        
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
