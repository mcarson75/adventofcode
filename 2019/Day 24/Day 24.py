import numpy as np

grid = np.array(
    [list(l.strip("\n")) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

MINUTES = 200

bugs = {x + y * 1j for (y, x) in np.argwhere(grid == "#")}
empty = {x + y * 1j for (y, x) in np.argwhere(grid == ".")}
dirs = {1, -1, 1j, -1j}


def repeating(bugs, empty):
    biodiversity = lambda p: int(2 ** (p.real + 5 * p.imag))
    allspace = bugs | empty
    adjacent = {p: {p + dir for dir in dirs} & allspace for p in allspace}

    visited = []
    while True:
        bugs = {b for b in bugs if len(adjacent[b] & bugs) == 1} | {
            e for e in empty if len(adjacent[e] & bugs) in [1, 2]
        }
        empty = allspace - bugs
        if bugs in visited:
            break
        visited.append(bugs)

    return sum([biodiversity(b) for b in bugs])


def recursive(initial, empty, minutes):
    allspace = initial | empty - {2 + 2j}
    adj = {p: {p + dir for dir in dirs} & allspace for p in allspace}
    adjacent = {p: {(0, i) for i in adj[p]} for p in adj}
    for dir in dirs:
        p = 2 + 2j + dir
        if dir in (1, -1):
            matching = {p + dir + i * 1j for i in range(-2, 3)}
        else:
            matching = {p + dir + i for i in range(-2, 3)}
        adjacent[p] |= {(1, m) for m in matching}
        for m in matching:
            adjacent[m].add((-1, p))

    bugs = {(0, bug) for bug in initial}
    for _ in range(minutes):
        layers = {l for l, _ in bugs}
        layers = set(range(min(layers) - 1, max(layers) + 2))
        empty = {(l, p) for l in layers for p in allspace} - bugs
        adj_adjacent = {
            (layer, k): {(layer + l, p) for l, p in v}
            for k, v in adjacent.items()
            for layer in layers
        }
        bugs = {b for b in bugs if len(adj_adjacent[b] & bugs) == 1} | {
            e for e in empty if len(adj_adjacent[e] & bugs) in [1, 2]
        }

    return len(bugs)


part1 = repeating(bugs, empty)
part2 = recursive(bugs, empty, MINUTES)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
