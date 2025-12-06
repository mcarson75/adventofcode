import numpy as np

grid = np.array(
    [list(l.strip("\n")) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

DIRS = {-1 - 1j, -1, -1 + 1j, 1j, -1j, 1 - 1j, 1, 1 + 1j}
removable = lambda rolls, loc: len(set(loc + d for d in DIRS) & rolls) < 4

rolls = {x + y * 1j for (y, x) in np.argwhere(grid == "@")}

part1 = part2 = 0
while True:
    rem = {roll for roll in rolls if removable(rolls, roll)}
    if part1 == 0:
        part1 = len(rem)
    if not rem:
        break
    part2 += len(rem)
    rolls -= rem

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
