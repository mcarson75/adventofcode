import re

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

gridsize = 4000000


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def merge_two_ranges(r1, r2):
    if r1.start <= r2.stop and r2.start <= r1.stop:
        return [range(min(r1.start, r2.start), max(r1.stop, r2.stop))]
    else:
        return [r1, r2]


def find_empty(sensors, y, restrict=[0, gridsize]):
    covered = []
    for s in sensors.keys():
        dist = sensors[s][1]
        if abs(s[1] - y) <= dist:
            dx = dist - abs(s[1] - y)
            x1, x2 = s[0] - dx, s[0] + dx + 1
            if restrict:
                x1 = max(x1, restrict[0])
                x2 = min(x2, restrict[1])

            covered.append(range(x1, x2))

    if covered:
        covered.sort(key=lambda r: r.start)
        i = 0
        while i < len(covered) - 1:
            r = merge_two_ranges(covered[i], covered[i + 1])
            covered[i : i + 2] = r
            if len(r) > 1:
                i += 1

    return covered


sensors = dict()

for l in lines:
    x1, y1, x2, y2 = [int(i) for i in re.findall("(-?\d+)", l)]
    sensors[(x1, y1)] = ((x2, y2), manhattan((x1, y1), (x2, y2)))

row = find_empty(sensors, 2000000, None)
part1 = len(row[0]) - len(set(b[0][0] for b in sensors.values() if b[0][1] == 2000000))

print(f"Part 1: {part1}")

for y in range(0, gridsize + 1):
    r = find_empty(sensors, y)
    if len(r) > 1:
        x = r[0].stop
        part2 = 4000000 * x + y
        break

print(f"Part 2: {part2}")
