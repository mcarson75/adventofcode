import numpy as np
from itertools import combinations

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)


def dist_shift(i, j, rowshift, colshift, wt):
    dist = abs(int((i - j).real)) + abs(int((i - j).imag))
    rows = set(range(int(min(i.imag, j.imag)), int(max(i.imag, j.imag))))
    cols = set(range(int(min(i.real, j.real)), int(max(i.real, j.real))))
    dist += len(rowshift & rows) * wt + len(colshift & cols) * wt
    return dist


gal = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))

rows_with_galaxies = set([int(y.imag) for y in gal])
rows = set(range(max(rows_with_galaxies))) - rows_with_galaxies

cols_with_galaxies = set([int(x.real) for x in gal])
cols = set(range(max(cols_with_galaxies))) - cols_with_galaxies

part1 = sum([dist_shift(a, b, rows, cols, 1) for a, b in combinations(gal, 2)])
part2 = sum([dist_shift(a, b, rows, cols, 999999) for a, b in combinations(gal, 2)])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
