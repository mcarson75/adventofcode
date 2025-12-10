import numpy as np
from collections import defaultdict
from itertools import count

grid = np.array(
    [list(l.rstrip("\n")) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

dirs = [1, -1, 1j, -1j]

map = {complex(x, y) for (y, x) in np.argwhere(grid == ".")}
limits = {
    "x": range(int(min(m.real for m in map)) + 1, int(max(m.real for m in map))),
    "y": range(int(min(m.imag for m in map)) + 1, int(max(m.imag for m in map))),
}
envelope = {x + y * 1j for x in limits["x"] for y in limits["y"]}

uppers = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
letters = {complex(x, y): grid[y, x] for (y, x) in np.argwhere(np.isin(grid, uppers))}

portals = {}
inner = {}
outer = {}
for letter in letters:
    for dir in dirs:
        if letter + dir in letters and letter - dir in map:
            if dir in {1, 1j}:
                portal = letters[letter] + letters[letter + dir]
            else:
                portal = letters[letter + dir] + letters[letter]
            if portal in portals:
                if letter - dir in envelope:
                    outer[portals[portal]] = letter - dir
                    inner[letter - dir] = portals[portal]
                else:
                    inner[portals[portal]] = letter - dir
                    outer[letter - dir] = portals[portal]

                del portals[portal]
            else:
                portals[portal] = letter - dir


def walk(start, finish, recurse=False):
    been = defaultdict(lambda: False)
    been[(start, 0)] = True
    q = [(start, 0)]
    for step in count(1):
        if not q:
            break
        cur, q = q, []
        for p, layer in cur:
            for np in [p + dir for dir in dirs]:
                nl = layer
                if np not in map:
                    if p in inner:
                        if not recurse:
                            np = inner[p]
                        if recurse and nl <= len(inner):
                            np = inner[p]
                            nl += 1
                    elif p in outer:
                        if not recurse:
                            np = outer[p]
                        if recurse and nl > 0:
                            np = outer[p]
                            nl -= 1
                if np in map and not been[(np, nl)]:
                    if np == finish and nl == 0:
                        return step
                    been[(np, nl)] = True
                    q.append((np, nl))


part1 = walk(portals["AA"], portals["ZZ"])
part2 = walk(portals["AA"], portals["ZZ"], recurse=True)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
