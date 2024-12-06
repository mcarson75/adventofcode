import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

visited = set(x + y * 1j for (y, x) in np.argwhere(grid == "^"))
obstacles = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))
dirs = [-1j, 1, 1j, -1]
starting_pos = pos = list(visited)[0]
dir = 0

MAX_X, MAX_Y = max([i.real for i in obstacles]), max([i.imag for i in obstacles])


def is_loop(pos, obstacle):
    dir = 0
    visited = set((pos, dir))
    while 0 < pos.real < MAX_X and 0 < pos.imag < MAX_Y:
        if pos + dirs[dir] not in (obstacles | {obstacle}):
            pos += dirs[dir]
            if (pos, dir) in visited:
                return True
            visited.add((pos, dir))
        else:
            dir += 1
            dir %= len(dirs)
    return False


while 0 < pos.real < MAX_X and 0 < pos.imag < MAX_Y:
    if pos + dirs[dir] not in obstacles:
        pos += dirs[dir]
        visited.add(pos)
    else:
        dir += 1
        dir %= len(dirs)

part1 = len(visited)
part2 = 0
for v in visited:
    if is_loop(starting_pos, v):
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
