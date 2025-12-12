from math import prod

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

shapes = []
regions = []

fits = lambda s, pr: prod(s) >= sum([p * shapes[i] for i, p in enumerate(pr)])
ssplit = lambda line, n, ch: [int(i) for i in line.split(": ")[n].split(ch)]

for line in lines:
    if ":" in line and "x" not in line:
        shapes.append(0)
    elif ":" in line and "x" in line:
        regions.append((ssplit(line, 0, "x"), ssplit(line, 1, " ")))
    else:
        shapes[-1] += line.count("#")

part1 = sum([fits(*r) for r in regions])

print(f"Part 1: {part1}")
