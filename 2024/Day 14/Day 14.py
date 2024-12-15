import re
from math import prod
from statistics import variance as var

W, H = 101, 103


def sub_quadrant(x, L):
    if x < (mid := (L - 1) // 2):
        return 0
    if x > mid:
        return 1
    return 4


robots = [
    [int(i) for i in re.findall(r"-?\d+", l.strip())]
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]


get_pos = lambda t: [
    ((sx + t * vx) % W, (sy + t * vy) % H) for (sx, sy, vx, vy) in robots
]


quadrant = lambda r: sub_quadrant(r[0], W) + 2 * sub_quadrant(r[1], H)

part1 = prod([[quadrant(r) for r in get_pos(100)].count(n) for n in range(4)])

b = lambda L, y: min(
    range(L),
    key=lambda t: var((s + t * v) % L for (s, v) in [r[y::2] for r in robots]),
)
bx = b(W, False)
by = b(H, True)

part2 = bx + ((pow(W, -1, H) * (by - bx)) % H) * W


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
