import numpy as np
from itertools import combinations

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

MAX_X = len(grid[0]) - 1
MAX_Y = len(grid) - 1

in_bounds = lambda pos: 0 <= pos.real <= MAX_X and 0 <= pos.imag <= MAX_Y
get_antinodes = lambda i, j, l: set([g for n in l if in_bounds(g := (i + n * (j - i)))])

antenna_types = set(np.unique(grid))
antenna_types.remove(".")

part1, part2 = set(), set()

for a in antenna_types:
    nodes = set(x + y * 1j for (y, x) in np.argwhere(grid == a))
    if len(nodes) > 1:
        for i, j in combinations(nodes, 2):
            part1 |= get_antinodes(i, j, [-1, 2])
            part2 |= get_antinodes(i, j, range(-MAX_X, MAX_X))

print(f"Part 1: {len(part1)}")
print(f"Part 2: {len(part2)}")
