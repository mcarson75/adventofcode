import re
from math import lcm

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

moons = [[], [], []]
moons_init = [[], [], []]
for line in lines:
    pos = [int(i) for i in re.findall(r"-?\d+", line)]
    for n in range(len(pos)):
        moons[n].append((pos[n], 0))
        moons_init[n].append((pos[n], 0))


cycles = [None] * 3
part1_pos = [None] * 3
for n in range(len(pos)):
    step = 0
    while cycles[n] is None:
        vel = [i[1] for i in moons[n]]
        pos = [i[0] for i in moons[n]]
        for m in range(len(pos)):
            vel[m] += sum(pos[m] < p for p in pos) - sum(pos[m] > p for p in pos)
        pos = [pos[i] + vel[i] for i in range(len(pos))]
        moons[n] = [(pos[i], vel[i]) for i in range(len(pos))]
        step += 1
        if step == 1000:
            part1_pos[n] = (pos, vel)
        if moons[n] == moons_init[n]:
            cycles[n] = step
            break
part1 = 0
for m in range(4):
    kin = sum([abs(i) for i in [part1_pos[dim][0][m] for dim in range(3)]])
    pot = sum([abs(i) for i in [part1_pos[dim][1][m] for dim in range(3)]])
    part1 += kin * pot


part2 = lcm(*cycles)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
