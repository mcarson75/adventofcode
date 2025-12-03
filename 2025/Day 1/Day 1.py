moves = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
moves = [int(m.replace("R", "").replace("L", "-")) for m in moves]

DIAL = 50

stops = [DIAL] + [sum(moves[: n + 1]) + DIAL for n in range(len(moves))]
part1 = [s % 100 for s in stops].count(0)

part2 = 0
for n in range(1, len(stops)):
    step = 1 if stops[n] > stops[n - 1] else -1
    array = [n % 100 for n in list(range(stops[n - 1] + step, stops[n] + step, step))]
    part2 += array.count(0)

# rotations = [s // 100 for s in stops]
# part2 = sum([abs(j - i) for i, j in zip(rotations[:-1], rotations[1:])])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
