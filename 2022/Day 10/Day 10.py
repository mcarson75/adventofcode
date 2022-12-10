with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

part1 = 0
deltas = [1]

for line in lines:
    deltas.append(0)
    if "addx" in line:
        deltas.append(int(line.split()[1]))

X = [sum(deltas[:n]) for n in range(0, len(deltas))]

cycles = [20, 60, 100, 140, 180, 220]
part1 = sum([c * X[c] for c in cycles])

print(f"Part 1: {part1}")

BLOCK = "\u2588"

pixels = "".join(
    [BLOCK if x - 1 <= (i % 40) <= x + 1 else " " for i, x in enumerate(X[1:])]
)

ends = list(range(40, 241, 40))
for e in ends:
    print(pixels[e - 40 : e])
