import numpy as np

STEPS_PART1 = 64
STEPS_PART2 = 26501365

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)


def complex_mod(c, m):
    return c.real % m + c.imag % m * 1j


ROWS = len(grid)
COLS = len(grid[0])

possible = set(x + y * 1j for (y, x) in np.argwhere(grid == "S"))
plots = set(x + y * 1j for (y, x) in np.argwhere(grid == ".")) | possible

dirs = [1, -1, 1j, -1j]
factors = []

for n in range(1, 1000):
    possible = set(
        p + d for p in possible for d in dirs if complex_mod(p + d, ROWS) in plots
    )

    if n == STEPS_PART1:
        part1 = len(possible)
    elif n == ROWS // 2 + ROWS * len(factors):
        factors.append(len(possible))
        if len(factors) == 3:
            break

delta0, delta1, delta2 = (
    factors[0],
    factors[1] - factors[0],
    factors[2] - 2 * factors[1] + factors[0],
)
part2 = (
    delta0
    + delta1 * (STEPS_PART2 // ROWS)
    + delta2 * ((STEPS_PART2 // ROWS) * ((STEPS_PART2 // ROWS) - 1) // 2)
)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
