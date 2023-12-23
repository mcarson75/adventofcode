from collections import defaultdict
from math import inf
from heapq import heappop, heappush

grid = [l.rstrip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def cost(matrix, lo, hi):
    # q format (cost, (x, y), (dx, dy))
    q = [(0, (0, 0), (0, 1)), (0, (0, 0), (1, 0))]
    costs = defaultdict(lambda: inf)
    target = (len(matrix) - 1, len(matrix[0]) - 1)
    while q:
        cost, (x, y), (dx, dy) = heappop(q)
        if (x, y) == target:
            return cost
        if cost > costs[((x, y), (dx, dy))]:
            continue
        for ndx, ndy in ((-dy, dx), (dy, -dx)):
            nc = cost
            for dist in range(1, hi + 1):
                nx, ny = x + ndx * dist, y + ndy * dist
                if 0 <= nx <= target[0] and 0 <= ny <= target[1]:
                    nc += int(matrix[nx][ny])
                    if dist < lo:
                        continue
                    k = ((nx, ny), (ndx, ndy))
                    if nc < costs[k]:
                        costs[k] = nc
                        heappush(q, (nc, (nx, ny), (ndx, ndy)))
    return -1


print(f"Part 1: {cost(grid, 1, 3)}")
print(f"Part 2: {cost(grid, 4, 10)}")
