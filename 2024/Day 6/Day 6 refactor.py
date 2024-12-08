import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

obstacles = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))
starting_pos = list(x + y * 1j for (y, x) in np.argwhere(grid == "^"))[0]
dirs = [-1j, 1, 1j, -1]

MAX_X, MAX_Y = max([i.real for i in obstacles]), max([i.imag for i in obstacles])
in_bounds = lambda pos: 0 < pos.real < MAX_X and 0 < pos.imag < MAX_Y
# visited = {}
obstructions = set()


def get_path(pos, dir, visited, obstacles):
    initial = len(visited) == 0
    visited.add((pos, dir))
    while in_bounds(pos):
        if pos + dirs[dir] not in obstacles:
            pos += dirs[dir]
            if (pos, dir) in visited:
                return True  # loop
            elif initial and (
                get_path(pos, dir, visited.copy(), obstacles | {pos + dirs[dir]})
            ):
                obstructions.add(pos + dirs[dir])
        else:
            dir += 1
            dir %= len(dirs)
        visited.add((pos, dir))
    if initial:
        return len(set([x[0] for x in list(visited) if len(x) > 1])), len(obstructions)
    return False


part1, part2 = get_path(starting_pos, 0, set(), obstacles)
# part2 = sum([get_path(starting_pos, v) for v in visited])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
