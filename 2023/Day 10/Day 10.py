import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

path = set(x + y * 1j for (y, x) in np.argwhere(grid == "S"))
grid_ = {x + y * 1j: grid[y, x] for (y, x) in np.argwhere(grid)}

path_change = {
    ("|", 1j): 1j,
    ("|", -1j): -1j,
    ("-", 1): 1,
    ("-", -1): -1,
    ("L", 1j): 1,
    ("L", -1): -1j,
    ("J", 1j): -1,
    ("J", 1): -1j,
    ("7", -1j): -1,
    ("7", 1): 1j,
    ("F", -1j): 1,
    ("F", -1): 1j,
}


start = loc = list(path)[0]
if grid_[start + 1] in "-J7" and grid_[start - 1j] in "|F7":
    dir = 1
    grid_[start] = "L"
elif grid_[start + 1] in "-J7" and grid_[start + 1j] in "|JL":
    dir = 1
    grid_[start] = "F"
elif grid_[start - 1] in "-LF" and grid_[start - 1j] in "|F7":
    dir = -1
    grid_[start] = "J"
elif grid_[start - 1] in "-LF" and grid_[start + 1j] in "|JL":
    dir = -1
    grid_[start] = "7"
elif grid_[start + 1] in "-J7" and grid_[start - 1] in "-FL":
    dir = 1
    grid_[start] = "-"
elif grid_[start - 1j] in "|FL" and grid_[start + 1j] in "|J7":
    dir = 1j
    grid_[start] = "|"

while True:
    loc += dir
    path.add(loc)
    pipe = grid_[loc]
    if loc == start:
        break
    dir = path_change[(pipe, dir)]

part1 = (len(path) + 1) // 2
print(f"Part 1: {part1}")

part2 = 0
inside = False
for y in range(int(max(grid_).imag) + 1):
    for x in range(int(max(grid_).real) + 1):
        loc = x + y * 1j
        if loc in path and grid_[loc] in "|JL":
            inside = not inside
        elif not loc in path and inside:
            part2 += 1

print(f"Part 2: {part2}")
