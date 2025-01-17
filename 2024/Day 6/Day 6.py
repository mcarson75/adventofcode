import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

obstacles = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))
starting_pos = list(x + y * 1j for (y, x) in np.argwhere(grid == "^"))[0]
dirs = [-1j, 1, 1j, -1]
dir = 0

MAX_X, MAX_Y = max([i.real for i in obstacles]), max([i.imag for i in obstacles])
in_bounds = lambda pos: 0 < pos.real < MAX_X and 0 < pos.imag < MAX_Y
obstructions = set()


def get_path(pos, obstacle=-1 - 1j):
    dir = 0
    visited = {(pos, dir)}
    while in_bounds(pos):
        if pos + dirs[dir] not in (obstacles | {obstacle}):
            pos += dirs[dir]
            if (pos, dir) in visited:
                obstructions.add(obstacle)
                return True
            visited.add((pos, dir))
        else:
            dir += 1
            dir %= len(dirs)
    if obstacle == -1 - 1j:
        return set([x[0] for x in list(visited) if len(x) > 1])
    return False


part1 = len(visited := get_path(starting_pos))
part2 = sum([get_path(starting_pos, v) for v in visited])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
