from collections import defaultdict
from functools import cache


@cache
def find_connections(net=frozenset()):
    best = net
    for start in computers:
        if start in net:
            continue
        if net - computers[start]:
            continue
        new = find_connections(net | {start})
        if len(new) > len(best):
            best = new

    return best


networks = set(
    tuple(l.strip().split("-"))
    for l in open("input.txt", "r", encoding="utf-8").readlines()
)

computers = defaultdict(set)
connected = set()

for net in networks:
    n1, n2 = net
    computers[n1].add(n2)
    computers[n2].add(n1)

for c1 in computers:
    for c2 in computers[c1]:
        for c3 in (computers[c2] - {c1}) & computers[c1]:
            connected.add(tuple(sorted((c1, c2, c3))))


part1 = len([comp for comp in connected if any([c.startswith("t") for c in comp])])

print(f"Part 1: {part1}")

conn = find_connections()
part2 = ",".join(sorted(list(conn)))

print(f"Part 2: {part2}")
