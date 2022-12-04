import re

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    x1, x2, y1, y2 = [int(i) for i in re.split("-|,", line)]

    r1 = set(range(x1, x2 + 1))
    r2 = set(range(y1, y2 + 1))

    part1 += int(r2.issubset(r1) or r1.issubset(r2))
    part2 += int(len(r2.intersection(r1)) > 0 or len(r1.intersection(r2)) > 0)


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
