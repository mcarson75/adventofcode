import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

infected = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))

pos = (len(grid[0]) - 1) // 2 + (len(grid) - 1) // 2 * 1j
moves = [-1j, 1, 1j, -1]
dir = 0
new_infections = 0

for _ in range(10000):
    if pos in infected:
        dir += 1
        infected.remove(pos)
    else:
        dir -= 1
        infected.add(pos)
        new_infections += 1
    dir %= 4
    pos += moves[dir]

print(f"Part 1: {new_infections}")

infected = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))
weakened = set()
flagged = set()
pos = (len(grid[0]) - 1) // 2 + (len(grid) - 1) // 2 * 1j
dir = 0
new_infections = 0


for _ in range(10000000):
    if pos in infected:
        dir += 1
        infected.remove(pos)
        flagged.add(pos)
    elif pos in weakened:
        weakened.remove(pos)
        infected.add(pos)
        new_infections += 1
    elif pos in flagged:
        dir += 2
        flagged.remove(pos)
    else:
        dir -= 1
        weakened.add(pos)
    dir %= 4
    pos += moves[dir]

print(f"Part 2: {new_infections}")
