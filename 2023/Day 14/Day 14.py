from collections import namedtuple
import numpy as np

ROLLS = 1000000000

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)


class Platform:
    Stone = namedtuple("Stone", "x y")

    def __init__(self, grid):
        self.height = len(grid)
        fixed = set(self.Stone(x, y) for (y, x) in np.argwhere(grid == "#"))
        self.fixed = self.get_fixed(fixed)
        self.moving = set(self.Stone(x, y) for (y, x) in np.argwhere(grid == "O"))
        self.first_load = None
        self.turns = 1
        self.cycling = False
        self.seen = {}

    def get_fixed(self, fixed):
        all_fixed = []
        for _ in range(4):
            this_fixed = []
            for i in range(self.height):
                f = [s.y for s in fixed if s.x == i]
                f = [-1] + sorted(f) + [self.height + 1]
                this_fixed.append(
                    [set(range(start, end)) for start, end in zip(f[:-1], f[1:])]
                )
            all_fixed.append(this_fixed)
            fixed = self.T(fixed)
        return all_fixed

    def do_turns(self, num_turns):
        while self.turns <= num_turns:
            self.one_turn()
            self.turns += 1
            s = str(self.moving)
            if not self.cycling and s in self.seen:
                repeat_period = self.turns - self.seen[s]
                self.turns = num_turns - ((num_turns - self.seen[s]) % repeat_period)
                self.cycling = True
            self.seen[s] = self.turns

    def one_turn(self):
        for i in range(4):
            self.roll(self.fixed[i])
            self.moving = self.T(self.moving)

    def roll(self, fixed):
        new = set()
        for x in range(self.height):
            f = fixed[x]
            m = set(s.y for s in self.moving if s.x == x)
            new |= set(self.Stone(x, y) for y in self.roll_one_line(f, m))
        self.moving = new
        if not self.first_load:
            self.first_load = self.load

    def roll_one_line(self, fixed, m):
        new = set()
        for f in fixed:
            new |= set(range(min(f) + 1, min(f) + len(f & m) + 1))

        return new

    @property
    def load(self):
        return sum([self.height - s.y for s in self.moving])

    def T(self, s):
        return set(self.Stone(self.height - y - 1, x) for (x, y) in s)


platform = Platform(grid)
platform.do_turns(ROLLS)

print(f"Part 1: {platform.first_load}")
print(f"Part 2: {platform.load}")
