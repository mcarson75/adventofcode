import sys
from math import inf
from heapq import heappop, heappush

sys.setrecursionlimit(3000)

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

for line in lines:
    type, value = line.split(":")
    if type == "depth":
        depth = int(value)
    elif type == "target":
        x, y = [int(n) for n in value.split(",")]
        target = complex(x, y)

erosions = {}


def geologic_index(coor):
    if coor == 0 or coor == target:
        return 0
    if coor.imag == 0:
        return int(coor.real) * 16807
    if coor.real == 0:
        return int(coor.imag) * 48271
    return erosion(coor - 1) * erosion(coor - 1j)


def erosion(coor):
    if coor not in erosions:
        erosions[coor] = (geologic_index(coor) + depth) % 20183
    return erosions[coor]


def risk(coor):
    return erosion(coor) % 3


erosion(target)
coords = (
    complex(x, y)
    for x in range(int(target.real) + 1)
    for y in range(int(target.imag) + 1)
)

risks = {z: risk(z) for z in coords}

print(f"Part 1: {sum(risks.values())}")

inbounds = (
    lambda p: p.real >= 0
    and p.imag >= 0
    and p.real < 3 * target.real
    and p.imag < 3 * target.imag
)
dirs = [1, -1, 1j, -1j]

# 0 = none (wet or narrow - 1 or 2)
# 1 = torch (rocky or narrow - 0 or 2)
# 2 = climbing gear (wet or rocky - 0 or 1)
valid_tool = {0: [1, 2], 1: [0, 2], 2: [0, 1]}  # soil: tool


def get_path(start, end):
    q = [(0, 0, start, 1)]
    costs = {(start, 1): 0}
    counter = 0
    seen = set()
    while q:
        cost, _, pos, tool = heappop(q)
        if (pos, tool) in costs and costs[(pos, tool)] < cost:
            continue
        if pos == end and tool == 1:
            return cost
        for p in {pos + d for d in dirs if inbounds(pos + d)}:
            if tool in valid_tool[risk(p)] and (new_cost := cost + 1) < costs.get(
                (p, tool), inf
            ):
                costs[(p, tool)] = new_cost
                if not (new_cost, p, tool) in seen:
                    counter += 1
                    seen.add((new_cost, p, tool))
                    heappush(q, (new_cost, counter, p, tool))
        for new_tool in {t for t in valid_tool[risk(pos)] if t is not tool}:
            if (new_cost := cost + 7) < costs.get((pos, new_tool), inf):
                if not (new_cost, pos, new_tool) in seen:
                    counter += 1
                    seen.add((new_cost, pos, new_tool))
                    heappush(q, (new_cost, counter, pos, new_tool))


part2 = get_path(0, target)

print(f"Part 2: {part2}")
