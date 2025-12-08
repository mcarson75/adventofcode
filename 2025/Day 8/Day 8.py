from math import prod

points = [
    tuple(int(i) for i in l.strip("\n").split(","))
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]

CONNECTIONS = 1000

distance = lambda a, b: (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2

distances = {}
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        a = points[i]
        b = points[j]
        distances[distance(a, b)] = set([a, b])

circuits = []
count = 0
for d in sorted(distances):
    count += 1
    match = [c for c in circuits if distances[d] & c]
    if match:
        circuits = [c for c in circuits if c not in match]
        new_circuit = set(distances[d])
        for c in match:
            new_circuit |= c
        circuits.append(new_circuit)
    else:
        circuits.append(distances[d])
    if count == CONNECTIONS:
        part1 = prod(sorted([len(c) for c in circuits], reverse=True)[:3])
    if len(circuits) == 1 and len(circuits[0]) == len(points):
        part2 = list(distances[d])[0][0] * list(distances[d])[1][0]
        break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
