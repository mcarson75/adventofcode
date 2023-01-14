import numpy as np

input = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)


class Combatant:
    def __init__(self, pos, grid, power=3):
        self.round = 0
        self.pos = pos
        self.grid = grid
        self.hit = 200
        self.destroyed = False
        self.power = power

    def __repr__(self):
        return f"{self.pos}-{self.hit}"

    @property
    def sort_order(self):
        return (self.pos.imag, self.pos.real)

    def surrounding(self, pos=None):
        pos = self.pos if not pos else pos
        return [pos + p for p in [-1j, -1, 1, 1j]]

    def attacked(self, power=3):
        self.hit -= power
        self.destroyed = self.hit <= 0
        return self.destroyed

    @property
    def in_range(self):
        return set(
            i
            for e in self.enemy
            for i in e.surrounding()
            if i in self.grid.valid
            and i not in self.grid.occupied
            or i == self.pos
            and not e.destroyed
        )

    @property
    def enemy(self):
        return self.grid.goblins if self in self.grid.elves else self.grid.elves

    def move(self):
        self.round += 1
        in_range = self.in_range
        if self.pos in in_range:
            return
        q = [(self.pos, 0)]
        paths = {self.pos: (0, None)}
        seen = set()
        occupied = self.grid.occupied
        while q:
            pos, dist = q.pop(0)
            for p in self.surrounding(pos):
                if p not in self.grid.valid or p in occupied:
                    continue
                if p not in paths or paths[p][0] > dist + 1:
                    paths[p] = (dist + 1, pos)
                if p in seen:
                    continue
                if not any(p == i[0] for i in q):
                    q.append((p, dist + 1))
            seen.add(pos)

        valid_moves = [
            (pos, dist) for pos, (dist, _) in paths.items() if pos in in_range
        ]
        closest = sorted(
            [p for p, d in valid_moves if d == min([d for p, d in valid_moves])],
            key=lambda i: (i.imag, i.real),
        )

        if closest and not self.pos in in_range:
            closest = closest[0]
            while paths[closest][0] > 1:
                closest = paths[closest][1]

            self.pos = closest

    def attack(self):
        opponents = [e for e in self.enemy if e.pos in self.surrounding()]
        if opponents:
            target = min(opponents, key=lambda e: (e.hit, e.sort_order))
            if target and target.attacked(self.power):
                self.enemy.remove(target)
                if not self.enemy:
                    return "win"
                elif self.enemy is self.grid.elves:
                    return "elf_died"
                else:
                    return "continue"


class Grid:
    def __init__(self, grid, elf_power):
        self.valid = set(x + y * 1j for (y, x) in np.argwhere(grid != "#"))
        self.walls = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))
        self.goblins = set(
            Combatant(x + y * 1j, self) for (y, x) in np.argwhere(grid == "G")
        )
        self.elves = set(
            Combatant(x + y * 1j, self, power=elf_power)
            for (y, x) in np.argwhere(grid == "E")
        )

    @property
    def occupied(self):
        return set(i.pos for i in self.elves | self.goblins if not i.destroyed)

    @property
    def combatants(self):
        return sorted(list(self.goblins | self.elves), key=lambda p: p.sort_order)

    @property
    def living_combatants(self):
        return set(c for c in self.elves | self.goblins if not c.destroyed)

    @property
    def score(self):
        rd = min([c.round for c in self.living_combatants])
        points = sum([c.hit for c in self.living_combatants])
        return rd * points

    def print(self, file):
        xmax = max([int(w.real) for w in self.walls])
        ymax = max([int(w.imag) for w in self.walls])
        output = np.full((xmax + 1, ymax + 1), ".")
        goblins = set(g.pos for g in self.goblins)
        elves = set(e.pos for e in self.elves)
        for y in range(ymax + 1):
            for x in range(xmax + 1):
                if x + y * 1j in self.walls:
                    output[y, x] = "#"
                elif x + y * 1j in goblins:
                    output[y, x] = "G"
                elif x + y * 1j in elves:
                    output[y, x] = "E"
            print("".join(output[y]), file=file)


def play_game(input, allow_elf_death=True, elf_power=3, printgrid=False):
    grid = Grid(input, elf_power)
    round = 0
    outfile = open("output.txt", "w")
    if printgrid:
        print(file=outfile)
        print(f"Round {round} complete", file=outfile)
        print(f"{len(grid.goblins)} goblins remaining", file=outfile)
        print(f"{len(grid.elves)} elves remaining", file=outfile)
        grid.print(outfile)

    while True:
        for c in grid.combatants:
            if c not in grid.living_combatants:
                continue
            c.move()
            attack = c.attack()
            if attack == "win":
                outfile.close()
                return grid.score
            elif not allow_elf_death and attack == "elf_died":
                return None
        round += 1
        if printgrid:
            print(file=outfile)
            print(f"Round {round} complete", file=outfile)
            print(f"{len(grid.goblins)} goblins remaining", file=outfile)
            print(f"{len(grid.elves)} elves remaining", file=outfile)
            grid.print(outfile)


part1 = play_game(input)

elf_power = 4
part2 = None
while not part2:
    part2 = play_game(input, allow_elf_death=False, elf_power=elf_power)
    elf_power += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
