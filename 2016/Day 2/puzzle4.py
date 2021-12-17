import numpy as np

moves = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

code = ''
pos = [0, 2]
keypad = [[None, None, 1, None, None],
          [None, 2, 3, 4, None, None],
          [5, 6, 7, 8, 9],
          [None, 'A', 'B', 'C', None],
          [None, None, 'D', None, None]]

def move(pos, d):
    global keypad
    new_pos = [pos[0], pos[1]]
    if d == 'R':
        new_pos[0] = min(new_pos[0]+1, 4)
    elif d == 'L':
        new_pos[0] = max(new_pos[0]-1, 0)
    elif d == 'U':
        new_pos[1] = max(new_pos[1]-1, 0)
    elif d == 'D':
        new_pos[1] = min(new_pos[1]+1, 4)
    
    if keypad[new_pos[1]][new_pos[0]] == None:
        return pos
    return new_pos
        
for m in moves:
    for c in m:
        pos = move(pos, c)
    code += str(keypad[pos[1]][pos[0]])
    
print(code)