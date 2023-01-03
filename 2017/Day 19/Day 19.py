import numpy as np

grid = np.array(
    [list(l.strip("\n")) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

path = {x + y * 1j: grid[y, x] for (y, x) in np.argwhere(grid != " ")}

pos = min(path.keys(), key=lambda i: i.imag)
dir = 1j
part1 = ""
part2 = 1

while True:
    pos += dir
    if pos not in path:
        break
    part2 += 1
    if path[pos].isalpha():
        part1 += path[pos]
    elif path[pos] == "+":
        if dir.imag:
            test = [-1, 1]
        else:
            test = [-1j, 1j]
        for t in test:
            if pos + t in path:
                dir = t
                break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
