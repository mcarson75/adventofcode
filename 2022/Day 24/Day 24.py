import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

valid = set((x - 1) + (y - 1) * 1j for (y, x) in np.argwhere(grid != "#"))
start = min(valid, key=lambda i: i.imag)
end = max(valid, key=lambda i: i.imag)

WIDTH = int(max(i.real for i in valid - {start, end})) + 1
HEIGHT = int(max(i.imag for i in valid - {start, end})) + 1
ITERATIONS = int(np.lcm(WIDTH, HEIGHT))

right = [
    set((x - 1 + t) % WIDTH + (y - 1) * 1j for (y, x) in np.argwhere(grid == ">"))
    for t in range(WIDTH)
]
left = [
    set((x - 1 - t) % WIDTH + (y - 1) * 1j for (y, x) in np.argwhere(grid == "<"))
    for t in range(WIDTH)
]
up = [
    set((x - 1) + (y - 1 - t) % HEIGHT * 1j for (y, x) in np.argwhere(grid == "^"))
    for t in range(HEIGHT)
]
down = [
    set((x - 1) + (y - 1 + t) % HEIGHT * 1j for (y, x) in np.argwhere(grid == "v"))
    for t in range(HEIGHT)
]

free = [
    valid - right[t % WIDTH] - left[t % WIDTH] - up[t % HEIGHT] - down[t % HEIGHT]
    for t in range(ITERATIONS)
]


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
        _pos = (
            set([pos + 1, pos - 1, pos + 1j, pos - 1j, pos])
            & free[new_move % ITERATIONS]
        )
        q += [(_p, new_move) for _p in _pos]


q = [(start, 0)]
move = part1 = get_best(q, end)
print(f"Part 1: {part1}")

q = [(end, move)]
move = get_best(q, start)
q = [(start, move)]
part2 = get_best(q, end)
print(f"Part 2: {part2}")
