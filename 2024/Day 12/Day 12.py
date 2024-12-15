import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

plant_types = set(np.unique(grid))

get_perimeter = lambda pos, plants: 4 - len(get_surrounding(pos, plants))
get_surrounding = lambda pos, plants: set(pos + d for d in [-1, 1j, 1, -1j]) & plants


def get_corners(pos, plants):
    dirs = [-1, -1 + 1j, 1j, 1 + 1j, 1, 1 - 1j, -1j, -1 - 1j, -1]
    b = [p in plants for p in [pos + d for d in dirs]]
    corners = sum([b[n : n + 3 : 2] == [False, False] for n in range(0, len(b) - 1, 2)])
    corners += sum(
        [b[n : n + 3] == [True, False, True] for n in range(0, len(b) - 1, 2)]
    )

    return corners


def search_region(plants):
    pos = next(iter(plants))
    region = {pos}
    q = get_surrounding(pos, plants)
    while q:
        region |= q
        q = {e for pos in q for e in get_surrounding(pos, plants)} - region

    area = len(region)
    perimeter = sum([get_perimeter(p, region) for p in region])
    corners = sum([get_corners(p, region) for p in region])

    return area * perimeter, area * corners, region


part1 = part2 = 0
for plant in plant_types:
    plants = set(x + y * 1j for (y, x) in np.argwhere(grid == plant))

    while plants:
        score, price, region = search_region(plants)
        plants -= region
        part1 += score
        part2 += price

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
