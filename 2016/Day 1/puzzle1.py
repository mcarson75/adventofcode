import numpy as np

turns = [l.strip().split(', ') for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

pos = np.array([0, 0])
dir = np.array([0, 1])

def change_dir(dir, turn):
    if turn == 'R':
        x = 0 if dir[1]==0 else 1 if dir[1]==1 else -1
        y = 0 if dir[0]==0 else -1 if dir[0]==1 else 1
        return [x, y]
    elif turn == 'L':
        x = 0 if dir[1]==0 else -1 if dir[1]==1 else 1
        y = 0 if dir[0]==0 else 1 if dir[0]==1 else -1
        return [x, y]
        
for t in turns:
    turn = t[0]
    dist = int(t[1:])
    dir = change_dir(dir, turn)
    pos = np.add(pos, np.multiply(dir, dist))

print(sum([abs(i) for i in pos]))