import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)


def get_edges(grid, slopes=True):
    dirs = [1, -1, 1j, -1j]
    path = set(x + y * 1j for (y, x) in np.argwhere(grid == "."))
    slope_dn = set(x + y * 1j for (y, x) in np.argwhere(grid == "v"))
    slope_rt = set(x + y * 1j for (y, x) in np.argwhere(grid == ">"))
    pos = min(path, key=lambda x: x.imag)
    end = max(path, key=lambda x: x.imag)

    edges = {}
    if slopes:
        for point in path:
            for p in set([point + d for d in dirs]) & path:
                edges.setdefault(point, set()).add((p, 1))
                edges.setdefault(p, set()).add((point, 1))
        for point in slope_rt:
            edges.setdefault(point, set()).add((point + 1, 1))
            edges.setdefault(point - 1, set()).add((point, 1))
        for point in slope_dn:
            edges.setdefault(point, set()).add((point + 1j, 1))
            edges.setdefault(point - 1j, set()).add((point, 1))
    else:
        path |= slope_dn | slope_rt
        for point in path:
            for p in set([point + d for d in dirs]) & path:
                edges.setdefault(point, set()).add((p, 1))
                edges.setdefault(p, set()).add((point, 1))
        while True:
            for k, v in edges.items():
                if len(v) == 2:
                    a, b = v
                    edges[a[0]].remove((k, a[1]))
                    edges[b[0]].remove((k, b[1]))
                    edges[a[0]].add((b[0], a[1] + b[1]))
                    edges[b[0]].add((a[0], a[1] + b[1]))
                    del edges[k]
                    break
            else:
                break
    return edges, pos, end


def longest_path(edges, pos, target):
    q = [(pos, 0)]
    visited = set()
    dist = 0
    while q:
        pos, d = q.pop()
        if d == -1:
            visited.remove(pos)
            continue
        if pos == target:
            dist = max(dist, d)
        if pos in visited:
            continue
        visited.add(pos)
        q.append((pos, -1))
        for p, l in edges[pos]:
            q.append((p, d + l))
    return dist


part1 = longest_path(*get_edges(grid))
print(f"Part 1: {part1}")

part2 = longest_path(*get_edges(grid, slopes=False))
print(f"Part 2: {part2}")
