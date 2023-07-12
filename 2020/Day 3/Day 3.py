import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

trees = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))
WIDTH = len(grid[0])
HEIGHT = len(grid)


def check_trees(x, y):
    pos = 0 + 0j
    num_trees = 0
    while pos.imag < HEIGHT:
        if pos in trees:
            num_trees += 1
        pos = (pos.real + x) % WIDTH + (pos.imag + y) * 1j

    return num_trees


part2 = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slope in slopes:
    part2 *= check_trees(slope[0], slope[1])

print(f"Part 1: {check_trees(3,1)}")
print(f"Part 2: {part2}")
