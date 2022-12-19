lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

cubes = set()
for l in lines:
    cubes.add(tuple([int(i) for i in l.split(",")]))


def adj_cubes(c):
    x, y, z = c
    return set(
        [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]
    )


area = 6 * len(cubes)
for c in cubes:
    area -= len(cubes.intersection(adj_cubes(c)))

print(f"Part 1: {area}")

min_xyz = tuple(min(c[i] for c in cubes) - 1 for i in range(3))
max_xyz = tuple(max(c[i] for c in cubes) + 1 for i in range(3))

q = [min_xyz]

visited = set()
area = 0
while q:
    c = q.pop()
    if c in visited:
        continue
    visited.add(c)
    for ci in adj_cubes(c):
        if ci in cubes:
            area += 1
        if (
            ci not in cubes
            and ci not in visited
            and all(l <= v <= u for l, v, u in zip(min_xyz, ci, max_xyz))
        ):
            q.append(ci)

print(f"Part 2: {area}")
