from math import inf

GRID_MAX = 70
SIM_TIME = 1024

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
    q = [(0, start)]
    costs = {start: 0}
    while q:
        cost, pos = q.pop(0)
        if pos == end:
            return cost
        for p in {pos + d for d in dirs if inbounds(pos + d)} - obstacles:
            if (new_cost := cost + 1) < costs.get(p, inf):
                costs[p] = new_cost
                if not (new_cost, p) in q:
                    q.append((new_cost, p))


current = step = SIM_TIME
while step > 1:
    obstacles = {complex(x, y) for (x, y) in bytes[:current]}
    if p := get_path(start, end):
        if current == SIM_TIME:
            part1 = p
        current += step
    else:
        step >>= 1
        current -= step

part2 = ",".join([str(i) for i in bytes[current - 1]])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
