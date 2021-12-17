import numpy as np

moves = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

code = ''
pos = [1, 1]
keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def move(pos, d):
    if d == 'R':
        pos[0] = min(pos[0]+1, 2)
    elif d == 'L':
        pos[0] = max(pos[0]-1, 0)
    elif d == 'U':
        pos[1] = max(pos[1]-1, 0)
    elif d == 'D':
        pos[1] = min(pos[1]+1, 2)
        
    return pos
        
for m in moves:
    for c in m:
        pos = move(pos, c)
    code += str(keypad[pos[1]][pos[0]])
    
print(code)