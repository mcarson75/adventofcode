from collections import deque
from itertools import permutations

with open("input.txt", 'r', encoding='utf-8') as f:
    maze = [l.strip() for l in f.readlines()]
    
# poi = set()
poi = []
hall = set()

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == '.':
            hall.add((j, i))
        elif maze[i][j].isnumeric():
            if maze[i][j] == '0':
                start = (j, i)
            else:
                poi.append((j, i))

def get_next_space(pos):
    x, y = pos
    moves = set([(-1, 0), (1, 0), (0, 1), (0, -1)])
    for dx, dy in moves:
        next_pos = (x + dx, y + dy)
        if next_pos in hall or next_pos in poi:
            yield next_pos

def bfs_from_to(fr, to):
    q = deque([(0, fr)])
    seen = set([fr])
    while q:
        dst, cur = q.pop()
        if cur == to:
            return dst
        for n in get_next_space(cur):
            if n not in seen:
                q.appendleft((dst + 1, n))
                seen.add(n)
    return -1

def get_paths():
    dst_0 = [bfs_from_to(start, n_pos) for n_pos in poi if n_pos != start]
    K = len(poi)
    dsts = [[None for j in range(K)] for i in range(K)]
    for i in range(K):
        for j in range(i + 1, K):
            dsts[j][i] = dsts[i][j] = bfs_from_to(poi[i], poi[j])

    part1, part2 = 1e12, 1e12
    for path in permutations(range(K)):
        dst = dst_0[path[0]]
        for i in range(len(path) - 1):
            dst += dsts[path[i]][path[i+1]]
        part1 = min(part1, dst)
        dst += dst_0[path[-1]]
        part2 = min(part2, dst)

    return part1, part2

part1, part2 = get_paths()

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))