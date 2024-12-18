from math import inf
from heapq import heappop, heappush

GRID_MAX = 70
SIM_TIME = 1024
# GRID_MAX = 6
# SIM_TIME = 12

bytes = [
    [int(i) for i in l.rstrip().split(",")]
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]

obstacles = {complex(x, y) for (x, y) in bytes[:SIM_TIME]}

inbounds = lambda x: 0 <= x.real <= GRID_MAX and 0 <= x.imag <= GRID_MAX

start = 0
end = complex(GRID_MAX, GRID_MAX)
dirs = [1, -1, 1j, -1j]


def get_path(start, end):
    q = [(0, 0, start)]
    costs = {start: 0}
    counter = 0
    while q:
        cost, _, pos = heappop(q)
        if pos == end:
            return cost
        for p in [pos + d for d in dirs]:
            if (
                p not in obstacles
                and inbounds(p)
                and (new_cost := cost + 1) < costs.get(p, inf)
            ):
                counter += 1
                costs[p] = new_cost
                if not (new_cost, p) in q:
                    heappush(q, (new_cost, counter, p))


part1 = get_path(start, end)

next_byte = SIM_TIME
while get_path(start, end):
    obstacles.add(complex(bytes[next_byte][0], bytes[next_byte][1]))
    next_byte += 1

part2 = ",".join([str(i) for i in bytes[next_byte - 1]])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
