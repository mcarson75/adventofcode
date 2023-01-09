serial = 3613

import numpy as np


def power(x, y, serial):
    rackid = x + 10
    power = (rackid * y + serial) * rackid // 100 % 10 - 5
    return power


grid = np.zeros((301, 301), dtype=int)
x = y = best_x = best_y = 1
for x in range(1, 301):
    for y in range(1, 301):
        grid[x, y] = power(x, y, serial)


def get_max(size):
    max_total = 0
    best_x = best_y = 0
    for x in range(1, 301 - size):
        for y in range(1, 301 - size):
            subgrid = grid[x : x + size, y : y + size]
            if (total := np.sum(subgrid)) > max_total:
                max_total = total
                best_x, best_y = x, y

    return (best_x, best_y), max_total


part1, _ = get_max(3)
print(f"Part 1: {part1}")

best_size = 0
max_total = 0
for size in range(1, 301):
    this, total = get_max(size)
    if total > max_total:
        max_total = total
        part2 = this
        best_size = size

print(f"Part 2: {part2}, {best_size}")
