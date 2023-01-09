serial = 3613

import numpy as np


def power(x, y, serial):
    rackid = x + 10
    power = (rackid * y + serial) * rackid // 100 % 10 - 5
    return power


grid = np.zeros((301, 301), dtype=int)
for x in range(1, 301):
    for y in range(1, 301):
        grid[x, y] = (
            power(x, y, serial) + grid[x - 1, y] + grid[x, y - 1] - grid[x - 1, y - 1]
        )


def get_max(size):
    max_total = 0
    best_x = best_y = None
    for x in range(1, 301 - size):
        for y in range(1, 301 - size):
            total = (
                grid[x, y]
                + grid[x + size, y + size]
                - grid[x, y + size]
                - grid[x + size, y]
            )
            if total > max_total:
                max_total = total
                best_x, best_y = x + 1, y + 1

    return best_x, best_y, max_total


x1, y1, _ = get_max(3)

max_total = 0
for size in range(1, 301):
    _x, _y, total = get_max(size)
    if total > max_total:
        max_total = total
        x2, y2 = _x, _y
        best_size = size

print(f"Part 1: {(x1,y1)}")
print(f"Part 2: {(x2,y2,best_size)}")
