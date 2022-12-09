import os
from collections import defaultdict

with open("input.txt", "r", encoding="utf-8") as f:
    coords = set([tuple(int(i) for i in l.strip().split(",")) for l in f.readlines()])

xrange = range(min([i[0] for i in coords]), max([i[0] for i in coords]) + 1)
yrange = range(min([i[1] for i in coords]), max([i[1] for i in coords]) + 1)

coord_id_to_point = {coord_id: point for coord_id, point in enumerate(coords, start=1)}

region_sizes = defaultdict(int)
infinite_ids = set()
size_shared_region = 0

for i in xrange:
    for j in yrange:
        min_dists = sorted(
            [
                (abs(r - i) + abs(c - j), coord_id)
                for coord_id, (r, c) in coord_id_to_point.items()
            ]
        )

        if len(min_dists) == 1 or min_dists[0][0] != min_dists[1][0]:
            coord_id = min_dists[0][1]
            region_sizes[coord_id] += 1

            if (
                i == min(xrange)
                or i == max(xrange)
                or j == min(yrange)
                or j == max(yrange)
            ):
                infinite_ids.add(coord_id)

        size_shared_region += int(
            sum(abs(r - i) + abs(c - j) for r, c in coords) < 10000
        )

part1 = max(
    size for coord_id, size in region_sizes.items() if coord_id not in infinite_ids
)

part2 = size_shared_region

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
