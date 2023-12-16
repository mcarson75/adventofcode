import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

mirrors = {x + y * 1j: grid[y, x] for (y, x) in np.argwhere(grid != ".")}

MAX_HEIGHT = len(grid)
MAX_WIDTH = len(grid[0])


def beam(loc, dir, seen):
    energized = set()
    while 0 <= loc.real <= MAX_WIDTH - 1 and 0 <= loc.imag <= MAX_HEIGHT - 1:
        if (loc, dir) in seen:
            return energized
        else:
            seen.add((loc, dir))
        energized.add(loc)
        if loc in mirrors:
            if mirrors[loc] == "-" and dir in [-1j, 1j]:
                energized |= beam(loc - 1, -1, seen)
                dir = 1
            elif mirrors[loc] == "|" and dir in [-1, 1]:
                energized |= beam(loc - 1j, -1j, seen)
                dir = 1j
            elif mirrors[loc] == "\\":
                dir = dir.imag + dir.real * 1j
            elif mirrors[loc] == "/":
                dir = -dir.imag - dir.real * 1j
        loc += dir
    return energized


part1 = len(beam(0, 1, set()))
print(f"Part 1: {part1}")

part2 = 0
for loc in range(MAX_WIDTH):
    part2 = max(part2, len(beam(loc, 1j, set())))
    part2 = max(part2, len(beam(loc * 1j, 1, set())))
    part2 = max(part2, len(beam(loc + (MAX_HEIGHT - 1) * 1j, -1j, set())))
    part2 = max(part2, len(beam(MAX_WIDTH - 1 + loc * 1j, -1, set())))

print(f"Part 2: {part2}")
