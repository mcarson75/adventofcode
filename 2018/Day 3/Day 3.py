from collections import defaultdict
import re

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

claims = map(lambda s: map(int, re.findall(r"-?\d+", s)), lines)
overlaps = {}
m = defaultdict(list)

for (claim, left, top, width, height) in claims:
    overlaps[claim] = set()
    for x in range(left, left + width):
        for y in range(top, top + height):
            if m[(x, y)]:
                for n in m[(x, y)]:
                    overlaps[n].add(claim)
                    overlaps[claim].add(n)
            m[(x, y)].append(claim)

overlap = len([i for i in m if len(m[i]) > 1])
freespace = [i for i in overlaps if len(overlaps[i]) == 0][0]

print(f"Part 1: {overlap}")
print(f"Part 2: {freespace}")
