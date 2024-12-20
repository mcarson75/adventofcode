import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

pts = {complex(x, y) for (y, x) in np.argwhere(grid == ".")}
start = [complex(x, y) for (y, x) in np.argwhere(grid == "S")][0]
end = [complex(x, y) for (y, x) in np.argwhere(grid == "E")][0]

pts.add(start)
pts.add(end)

circle = lambda pos, size: {
    pos + complex(i, j)
    for n in range(size + 1)
    for i in (n, -n)
    for j in (size - n, n - size)
}


def order(pts, start):
    pos = start
    i = 0
    ordered = {start: i}
    pts.remove(start)
    while pts:
        pos = (circle(pos, 1) & pts).pop()
        pts.remove(pos)
        ordered[pos] = (i := i + 1)
    return ordered


path = order(pts, start)

part1 = part2 = 0
for p in path:
    for size in range(2, 21):
        valid = lambda n: n in path and path[n] - path[p] - size >= 100
        if size == 2:
            part1 += sum(valid(n) for n in circle(p, size))
        part2 += sum(valid(n) for n in circle(p, size))


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
