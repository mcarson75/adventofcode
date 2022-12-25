import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

empty = set(x + y * 1j - 1 - 1j for (y, x) in np.argwhere(grid == "."))
start = min(empty, key=lambda i: i.imag)
end = max(empty, key=lambda i: i.imag)

WIDTH = int(max(i.real for i in empty - {start, end})) + 1
HEIGHT = int(max(i.imag for i in empty - {start, end})) + 1
ITERATIONS = int(np.lcm(WIDTH, HEIGHT))

right = [
    [(x - 1 + t) % WIDTH + (y - 1) * 1j for (y, x) in np.argwhere(grid == ">")]
    for t in range(WIDTH)
]
left = [
    [(x - 1 - t) % WIDTH + (y - 1) * 1j for (y, x) in np.argwhere(grid == "<")]
    for t in range(WIDTH)
]
up = [
    [(x - 1) + (y - 1 - t) % HEIGHT * 1j for (y, x) in np.argwhere(grid == "^")]
    for t in range(HEIGHT)
]
down = [
    [(x - 1) + (y - 1 + t) % HEIGHT * 1j for (y, x) in np.argwhere(grid == "v")]
    for t in range(HEIGHT)
]

blocked = {}
for t in range(ITERATIONS):
    blocked[t] = (
        set(right[t % WIDTH])
        | set(left[t % WIDTH])
        | set(up[t % HEIGHT])
        | set(down[t % HEIGHT])
    )


grid = blocked[0] | empty


def get_best(q, end):
    seen = set()
    while True:
        pos, move = q.pop(0)
        if pos == end:
            return move
        if (pos, move) in seen:
            continue
        seen.add((pos, move))
        new_move = move + 1

        for _pos in [pos + 1, pos - 1, pos + 1j, pos - 1j, pos]:
            if _pos in grid and _pos not in blocked[new_move % ITERATIONS]:
                q.append((_pos, new_move))


q = [(start, 0)]
part1 = get_best(q, end)
print(f"Part 1: {part1}")

q = [(end, part1)]
move = get_best(q, start)
q = [(start, move)]
part2 = get_best(q, end)
print(f"Part 2: {part2}")
