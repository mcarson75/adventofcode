import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

mirrors = {x + y * 1j: grid[y, x] for (y, x) in np.argwhere(grid != ".")}

MAX_HEIGHT = len(grid)
MAX_WIDTH = len(grid[0])


def beam(loc, dir, energized):
    while 0 <= loc.real <= MAX_WIDTH - 1 and 0 <= loc.imag <= MAX_HEIGHT - 1:
        if (loc, dir) in energized:
            return energized
        energized.add((loc, dir))
        if loc in mirrors:
            if mirrors[loc] == "-" and dir in [-1j, 1j]:
                energized |= beam(loc - 1, -1, energized)
                dir = 1
            elif mirrors[loc] == "|" and dir in [-1, 1]:
                energized |= beam(loc - 1j, -1j, energized)
                dir = 1j
            elif mirrors[loc] == "\\":
                dir = dir.imag + dir.real * 1j
            elif mirrors[loc] == "/":
                dir = -dir.imag - dir.real * 1j
        loc += dir
    return energized


def energized(loc, dir):
    return len(set([e[0] for e in beam(loc, dir, set())]))


print(f"Part 1: {energized(0,1)}")

start = set((l, 1j) for l in range(MAX_HEIGHT))
start |= set((l * 1j, 1) for l in range(MAX_WIDTH))
start |= set((l + (MAX_HEIGHT - 1) * 1j, -1j) for l in range(MAX_HEIGHT))
start |= set((MAX_WIDTH - 1 + l * 1j, -1) for l in range(MAX_WIDTH))

part2 = max([energized(s[0], s[1]) for s in start])

print(f"Part 2: {part2}")
