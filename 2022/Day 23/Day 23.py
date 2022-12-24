import numpy as np
from time import time

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

elves = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))
moves = [-1j, 1j, -1, 1]

adjacent = lambda p: set(
    [p - 1j, p + 1 - 1j, p + 1, p + 1 + 1j, p + 1j, p - 1 + 1j, p - 1, p - 1 - 1j]
)

adj_direction = lambda p, d: set(
    [p + d + (j * 1j) if not d.imag else p + d + j for j in [-1, 0, 1]]
)


def do_move(turn):
    global elves
    new_elves = {}
    for elf in elves:
        if elves & adjacent(elf):
            for move in moves[turn % 4 :] + moves[: turn % 4]:
                if not elves & adj_direction(elf, move):
                    new_elf = elf + move
                    if new_elf in new_elves:
                        del new_elves[new_elf]
                    else:
                        new_elves[new_elf] = elf
                    break

    if not new_elves:
        return True

    if turn % 25 == 0:
        print(f"Round {turn}: {len(new_elves)} elves moved")

    elves -= set(new_elves.values())
    elves |= set(new_elves.keys())

    return False


start = time()
turn, finished = 0, False
while not finished:
    finished = do_move(turn)
    turn += 1

    if turn == 10:
        total_area = (max(e.real for e in elves) - min(e.real for e in elves) + 1) * (
            max(e.imag for e in elves) - min(e.imag for e in elves) + 1
        )

        part1 = int(total_area) - len(elves)

print(f"Part 1: {part1}")
print(f"Part 2: {turn}")
print(f"    Time: {time()-start} s")
