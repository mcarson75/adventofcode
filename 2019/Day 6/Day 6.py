lines = [
    l.strip().split(")") for l in open("input.txt", "r", encoding="utf-8").readlines()
]

orbits = {k: v for k, v in lines}
orbits_lookup = {v: k for k, v in lines}

chains = {}

for o in orbits_lookup.keys():
    v = orbits_lookup[o]
    chain = [orbits_lookup[o]]

    while v != "COM":
        v = orbits_lookup[v]
        chain.append(v)
    chains[o] = chain

part1 = sum([len(v) for (k, v) in chains.items()])
for orbit in chains["SAN"]:
    if orbit in chains["YOU"]:
        part2 = chains["SAN"].index(orbit) + chains["YOU"].index(orbit)
        break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
