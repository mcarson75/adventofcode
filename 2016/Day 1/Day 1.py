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
        
visited = set()
visited.add((0,0))

part2 = False        
for t in turns:
    turn = t[0]
    dist = int(t[1:])
    dir = change_dir(dir, turn)
    for _ in range(dist):
        pos = np.add(pos, dir)
        p = (pos[0], pos[1])
        if not p in visited:
            visited.add(p)
        elif not part2:
            part2 = sum([abs(i) for i in pos])

part1 = sum([abs(i) for i in pos])

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))