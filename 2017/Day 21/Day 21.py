import numpy as np

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

mappings = {}
start = ".#./..#/###"


def translate_to_np(s):
    return np.array([[c == "#" for c in l] for l in s.split("/")])


for l in lines:
    source, repl = map(translate_to_np, l.split(" => "))
    for a in (source, np.fliplr(source)):
        for r in range(4):
            this = "".join([str(int(i)) for i in np.rot90(a, r).flatten()])
            mappings[this] = repl


def enhance(grid):
    size = len(grid)
    by = 2 if size % 2 == 0 else 3
    resize = lambda x: x * (by + 1) // by
    new_size = resize(size)
    solution = np.empty((new_size, new_size), dtype=bool)
    squares = range(0, size, by)
    new_squares = range(0, new_size, by + 1)

    for i, ni in zip(squares, new_squares):
        for j, nj in zip(squares, new_squares):
            square = "".join(
                [str(int(i)) for i in grid[i : i + by, j : j + by].flatten()]
            )
            enhanced = mappings[square]
            solution[ni : ni + by + 1, nj : nj + by + 1] = enhanced
    return solution


def solve(iterations):
    grid = translate_to_np(start)
    for _ in range(iterations):
        grid = enhance(grid)
    return int(grid.sum())


print(f"Part 1: {solve(5)}")
print(f"Part 2: {solve(18)}")
