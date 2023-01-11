import numpy as np

grid = np.array(
    [list(l.strip("\n")) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)


class Cart:
    turns = [-1, 0, 1]
    dirs = {"^": -1j, "<": -1, "v": 1j, ">": 1}

    def __init__(self, pos: complex, aim: str):
        self.pos = pos
        self.dir = self.dirs[aim]
        self.turn_index = 0
        self.destroyed = False

    def turn(self, t):
        if t:
            self.dir *= t * 1j

    @property
    def next_pos(self):
        return self.pos + self.dir

    def move(self):
        self.pos += self.dir
        p = path[self.pos]
        if p == "+":
            self.turn(self.turns[self.turn_index])
            self.turn_index += 1
            self.turn_index %= 3
        elif p == "/":
            self.turn(1) if self.dir.real == 0 else self.turn(-1)
        elif p == "\\":
            self.turn(-1) if self.dir.real == 0 else self.turn(1)


path = {x + y * 1j: grid[y, x] for (y, x) in np.argwhere(grid != " ")}
carts = list(Cart(k, v) for k, v in path.items() if v in ["v", "^", "<", ">"])
for c in carts:
    path[c.pos] = "-" if c.dir.real != 0 else "|"

part1 = None
while True:
    carts.sort(key=lambda c: (c.pos.imag, c.pos.real))
    for c in carts:
        c.move()
        if len(destroyed := [i for i in carts if i.pos == c.pos]) > 1:
            if not part1:
                part1 = c.pos
            for i in destroyed:
                i.destroyed = True
    carts = [c for c in carts if not c.destroyed]
    if len(carts) == 1:
        part2 = carts[0].pos
        break

print(f"Part 1: {int(part1.real)}, {int(part1.imag)}")
print(f"Part 2: {int(part2.real)}, {int(part2.imag)}")
