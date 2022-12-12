import numpy as np

inr = lambda pos, arr: pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
matrix = np.array([list(l) for l in lines])

start = np.argwhere(matrix == "S")[0]
end = np.argwhere(matrix == "E")[0]

matrix[tuple(start)] = "a"
matrix[tuple(end)] = "z"


def get_best(q):
    costs = {}
    while True:
        cost, x, y = q[0]
        if (x, y) == tuple(end):
            return cost
        q = q[1:]
        for _x, _y in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
            if inr((_x, _y), matrix):
                nc = cost + 1
                if (_x, _y) in costs and costs[(_x, _y)] <= nc:
                    continue
                test = ord(matrix[x, y])
                if ord(matrix[_x, _y]) <= test + 1:
                    costs[(_x, _y)] = nc
                    q.append((nc, _x, _y))
        q = sorted(q)


q = [(0, start[0], start[1])]
part1 = get_best(q)
print(f"Part 1: {part1}")

q = []
start = np.argwhere(matrix == "a")
for s in start:
    q.append((0, s[0], s[1]))

part2 = get_best(q)
print(f"Part 2: {part2}")
