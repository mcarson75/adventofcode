import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

locations = {x + y * 1j: int(grid[y, x]) for (y, x) in np.argwhere(grid)}
part1 = part2 = 0


def check_next(location, value):
    trailends = set()
    rating = 0
    for dir in [-1, 1, -1j, 1j]:
        if location + dir in locations:
            nxt = locations[location + dir]
            if nxt == value + 1:
                if value == 8:
                    trailends.add(location + dir)
                    rating += 1
                else:
                    t, r = check_next(location + dir, nxt)
                    rating += r
                    trailends |= t
    return trailends, rating


for location in locations:
    if locations[location] == 0:
        t, r = check_next(location, 0)
        part1 += len(t)
        part2 += r

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
