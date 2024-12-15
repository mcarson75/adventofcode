import numpy as np

map = {"<": -1, ">": 1, "^": -1j, "v": 1j}

grid, moves = [l for l in open("input.txt", "r", encoding="utf-8").read().split("\n\n")]

grid = np.array([list(l) for l in grid.split("\n")])
moves = [map[i] for i in moves.replace("\n", "")]

score = lambda b: int(b.real + 100 * b.imag)
double = lambda c: 2 * c.real + c.imag * 1j


def find_box(pos, boxes, obstacles, m):
    new_box = set()
    if pos in obstacles:
        return True, new_box
    stopped = False
    for box in boxes:
        if pos in box:
            new_box.add(box)
            for b in box:
                if b + m not in box:
                    s, n = find_box(b + m, boxes, obstacles, m)
                    stopped = s or stopped
                    new_box |= n
    return stopped, new_box


def do_moves(grid, moves, single=True):
    obstacles = {x + y * 1j for (y, x) in np.argwhere(grid == "#")}
    boxes = {(x + y * 1j,) for (y, x) in np.argwhere(grid == "O")}
    pos = [x + y * 1j for (y, x) in np.argwhere(grid == "@")][0]

    if not single:
        obstacles = {double(o) for o in obstacles}
        obstacles |= {o + 1 for o in obstacles}
        boxes = {(double(b), double(b) + 1) for (b,) in boxes}
        pos = double(pos)

    for m in moves:
        stopped, box_set = find_box(pos + m, boxes, obstacles, m)
        if not stopped:
            new_boxes = set(tuple(b + m for b in box) for box in box_set)
            boxes -= box_set
            boxes |= new_boxes
            pos += m
    return boxes


part1 = sum([score(b[0]) for b in do_moves(grid, moves)])
part2 = sum([score(b[0]) for b in do_moves(grid, moves, single=False)])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
