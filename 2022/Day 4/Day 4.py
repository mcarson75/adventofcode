import re

pattern = r"(\d+)-(\d+),(\d+)-(\d+)"

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    m = re.match(pattern, line)

    x1, x2, y1, y2 = [int(i) for i in list(m.group(1, 2, 3, 4))]

    r1 = range(x1, x2 + 1)
    r2 = range(y1, y2 + 1)

    part1 += int(y1 in r1 and y2 in r1) or (x1 in r2 and x2 in r2)
    part2 += int(y1 in r1 or y2 in r1) or (x1 in r2 or x2 in r2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
