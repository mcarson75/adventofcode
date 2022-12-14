lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

blocked = set()
for line in lines:
    corners = [tuple(int(x) for x in i.split(",")) for i in line.split(" -> ")]
    for a, b in zip(corners, corners[1:]):
        minx, maxx = min(a[0], b[0]), max(a[0], b[0])
        miny, maxy = min(a[1], b[1]), max(a[1], b[1])
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                blocked.add((x, y))

bottom = max([r[1] for r in blocked]) + 1

sx, sy = 500, 0
part1 = 0
part2 = 0
reached_bottom = False

while (500, 0) not in blocked:
    if sy == bottom - 1:
        reached_bottom = True
    if (sx, sy + 1) not in blocked and sy < bottom:
        sy += 1
    elif (sx - 1, sy + 1) not in blocked and sy < bottom:
        sx -= 1
        sy += 1
    elif (sx + 1, sy + 1) not in blocked and sy < bottom:
        sx += 1
        sy += 1
    else:
        blocked.add((sx, sy))
        sx, sy = 500, 0
        if not reached_bottom:
            part1 += 1
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
