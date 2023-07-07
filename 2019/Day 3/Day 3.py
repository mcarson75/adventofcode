wires = [
    l.strip().split(",") for l in open("input.txt", "r", encoding="utf-8").readlines()
]

move = {"R": 1, "L": -1, "U": 1j, "D": -1j}

points = []
for w in wires:
    pts = [0]
    for dir in w:
        d = dir[0]
        dist = int(dir[1:])

        for n in range(dist):
            pts.append(pts[-1] + move[d])
    points.append(pts)

intersect = set(points[0]) & set(points[1])
intersect.remove(0)
dist = [int(abs(n.real) + abs(n.imag)) for n in intersect]

print(f"Part 1: {min(dist)}")

min_steps = 1e6
for i in intersect:
    min_steps = min(min_steps, points[0].index(i) + points[1].index(i))

print(f"Part 2: {min_steps}")
