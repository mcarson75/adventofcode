import numpy as np

grid = np.array(
    [list(l.strip("\n")) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

splitters = {x + y * 1j for (y, x) in np.argwhere(grid == "^")}
start = int([x for (y, x) in np.argwhere(grid == "S")][0])

part1 = 0
beams = {start: 1}
for row in range(len(grid)):
    s = {int(s.real) for s in splitters if s.imag == row}
    beam_hits = set(beams) & s
    part1 += len(beam_hits)
    for beam in beam_hits:
        beams[beam - 1] = beams.get(beam - 1, 0) + beams[beam]
        beams[beam + 1] = beams.get(beam + 1, 0) + beams[beam]
        beams.pop(beam, None)

part2 = sum(beams.values())

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
