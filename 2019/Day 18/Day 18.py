import numpy as np
from collections import defaultdict
from itertools import count

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

lowers = np.array(list("abcdefghijklmnopqrstuvwxyz"))
uppers = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
dirs = [1, -1, 1j, -1j]

map = set(complex(x, y) for (y, x) in np.argwhere(grid != "#"))
pos = [complex(x, y) for (y, x) in np.argwhere(grid == "@")][0]
keys = {complex(x, y): grid[y, x] for (y, x) in np.argwhere(np.isin(grid, lowers))}
doors = {complex(x, y): grid[y, x] for (y, x) in np.argwhere(np.isin(grid, uppers))}
robots = {pos + 1 + 1j: "1", pos + 1 - 1j: "2", pos - 1 + 1j: "3", pos - 1 - 1j: "4"}

cache = {}


def find_links(map, pos):
    links = {}
    walk = defaultdict(lambda: [99999, {}])
    walk[pos] = (0, set())
    q = [(pos, set())]

    for step in count(1):
        if not q:
            break
        newq, q = q, []
        for p, ds in newq:
            for np in [p + dir for dir in dirs]:
                if np not in map or walk[np][0] <= step:
                    continue
                if np in keys:
                    links[keys[np]] = (step, ds)
                nds = set(ds)
                if np in doors:
                    nds |= {doors[np].lower()}
                walk[np] = (step, nds)
                q.append((np, nds))
    return links


def get_shortest(names, needed):
    if not needed:
        return 0

    key = "".join(sorted(names)) + "".join(sorted(needed))
    if key in cache:
        return cache[key]

    shortest = float("inf")
    for k in needed:
        for k2 in names:
            if k not in links[k2]:
                continue

            l, closed = links[k2][k]
            if l >= shortest:
                continue
            if not closed.isdisjoint(needed):
                continue
            tail = get_shortest((names - {k2}) | {k}, needed - {k})
            shortest = min(shortest, l + tail)
    cache[key] = shortest
    return shortest


links = {k: find_links(map, p) for p, k in keys.items()} | {"@": find_links(map, pos)}
part1 = get_shortest({"@"}, set(keys.values()))

cache = {}
map -= set((pos + dir for dir in dirs)) | {pos}

links = {k: find_links(map, p) for p, k in keys.items()} | {
    k: find_links(map, p) for p, k in robots.items()
}
part2 = get_shortest(set(robots.values()), set(keys.values()))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
