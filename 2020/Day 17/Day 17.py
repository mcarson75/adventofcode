import numpy as np
from copy import deepcopy

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

cubes = set((x, y, 0, 0) for (y, x) in np.argwhere(grid == "#"))


def get_surrounding(cubes, coord):
    active = 0
    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            for z in range(coord[2] - 1, coord[2] + 2):
                for w in range(coord[3] - 1, coord[3] + 2):
                    if (x, y, z, w) != coord and (x, y, z, w) in cubes:
                        active += 1

    return active


def get_ranges(cubes):
    x = set([c[0] for c in cubes])
    y = set([c[1] for c in cubes])
    z = set([c[2] for c in cubes])
    w = set([c[3] for c in cubes])

    return (
        range(min(x) - 1, max(x) + 2),
        range(min(y) - 1, max(y) + 2),
        range(min(z) - 1, max(z) + 2),
        range(min(w) - 1, max(w) + 2),
    )


def get_cubes(cubes, dim):
    for iter in range(6):
        xrange, yrange, zrange, wrange = get_ranges(cubes)
        if dim == 3:
            wrange = range(1)
        new_cubes = deepcopy(cubes)
        for x in xrange:
            for y in yrange:
                for z in zrange:
                    for w in wrange:
                        active = get_surrounding(cubes, (x, y, z, w))
                        if (x, y, z, w) in cubes and active not in [2, 3]:
                            new_cubes.remove((x, y, z, w))
                        elif (x, y, z, w) not in cubes and active == 3:
                            new_cubes.add((x, y, z, w))
        cubes = new_cubes

    return len(cubes)


part1 = get_cubes(cubes, 3)
part2 = get_cubes(cubes, 4)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
