import numpy as np
from collections import defaultdict
from math import inf
from heapq import heappop, heappush

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

obstacles = {complex(x, y) for (y, x) in np.argwhere(grid == "#")}
start = [complex(x, y) for (y, x) in np.argwhere(grid == "S")][0]
end = [complex(x, y) for (y, x) in np.argwhere(grid == "E")][0]

getpreds = lambda pos: preds[pos].union(*[getpreds(p) for p in preds[pos]])
new_pos = lambda pos, dir: [
    (1 if d == dir else 1001, (pos + d, d))
    for d in [dir, 1j * dir, -1j * dir]
    if pos + d not in obstacles
]


def get_best(start, end):
    state = (start, 1)
    q = [(0, 0, state)]
    costs = {state: 0}
    counter = 0
    predecessors = defaultdict(set)
    predecessors[state] = set()
    while q:
        cost, _, state = heappop(q)
        pos, dir = state
        if pos == end:
            return cost, predecessors
        for nc, ns in new_pos(pos, dir):
            if (new_cost := cost + nc) < costs.get(ns, inf):
                counter += 1
                costs[ns] = new_cost
                if ns[0] == end:
                    predecessors[end].add(state)
                else:
                    predecessors[ns].add(state)
                if not (new_cost, counter, ns) in q:
                    heappush(q, (new_cost, counter, ns))


part1, preds = get_best(start, end)
part2 = 1 + len(set([x[0] for x in getpreds(end)]))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
