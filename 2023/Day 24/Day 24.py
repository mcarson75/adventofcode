import re
from itertools import combinations

LO = 200000000000000
HI = 400000000000000

stones = [
    [int(i) for i in re.findall("(-?\d+)", l)]
    for l in open("input.txt", "r", encoding="utf-8")
]

stone_mb = {}
for stone in stones:
    x, y, z, dx, dy, dz = stone
    m = dy / dx
    b = y - (m * x)
    stone_mb[(x, y, z, dx, dy, dz)] = (m, b)

part1 = 0
pv = [set()] * 3
for s1, s2 in combinations(stone_mb, 2):
    m1, b1 = stone_mb[s1]
    m2, b2 = stone_mb[s2]
    if m1 != m2:
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        t1 = (x - s1[0]) / s1[3]
        t2 = (x - s2[0]) / s2[3]
        if LO <= x <= HI and LO <= y <= HI and t1 > 0 and t2 > 0:
            part1 += 1
    for dir in range(3):
        p1, v1 = s1[dir], s1[dir + 3]
        p2, v2 = s2[dir], s2[dir + 3]
        if v1 == v2 and abs(v1) > 100:
            NewSet = set()
            d = p2 - p1
            for v in range(-1000, 1000):
                if v == v1:
                    continue
                if d % (v - v1) == 0:
                    NewSet.add(v)
            if pv[dir]:
                pv[dir] &= NewSet
            else:
                pv[dir] = NewSet.copy()
            if len(pv[dir]) == 1:
                continue

rdx, rdy, rdz = [p.pop() for p in pv]
ax, ay, az, adx, ady, adz = stones[0]
bx, by, bz, bdx, bdy, bdz = stones[1]
ma = (ady - rdy) / (adx - rdx)
mb = (bdy - rdy) / (bdx - rdx)
ba = ay - (ma * ax)
bb = by - (mb * bx)
x = int((bb - ba) / (ma - mb))
y = int(ma * x + ba)
t = (x - ax) // (adx - rdx)
z = az + (adz - rdz) * t

part2 = x + y + z
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
