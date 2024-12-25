input = [l for l in open("input.txt", "r", encoding="utf-8").read().split("\n\n")]

locks = list()
keys = list()

for poss in input:
    poss = poss.splitlines()
    combo = [sum([p[n] == "#" for p in poss]) - 1 for n in range(len(poss[0]))]
    if poss[0] == "#####":
        locks.append(combo)
    else:
        keys.append(combo)

part1 = 0
for lock in locks:
    for key in keys:
        part1 += all([key[i] + lock[i] <= 5 for i in range(len(key))])


print(f"Part 1: {part1}")
