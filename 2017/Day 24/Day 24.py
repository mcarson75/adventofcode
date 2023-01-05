from collections import defaultdict


def gen_bridges(library, bridge=None):
    l, s, components, a = bridge or (0, 0, set(), 0)
    for b in library[a]:
        next = (a, b) if a <= b else (b, a)
        if next not in components:
            new = l + 1, s + a + b, (components | {next}), b
            yield new
            yield from gen_bridges(library, new)


nodes = set(
    tuple(int(i) for i in l.rstrip().split("/"))
    for l in open("input.txt", "r", encoding="utf-8").readlines()
)

library = defaultdict(set)
for a, b in nodes:
    library[a].add(b)
    library[b].add(a)

bridges = [b[:2] for b in gen_bridges(library)]
part1 = sorted(bridges, key=lambda x: x[1])[-1][1]
part2 = sorted(bridges)[-1][1]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
