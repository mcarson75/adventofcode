import re
from math import lcm

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

map_regex = r"(\w{3}) = \((\w{3}), (\w{3})\)"
instructions = [int(c) for c in lines[0].replace("L", "0").replace("R", "1")]
nodes = {}


def get_map(current_node, i):
    total = 0
    while True:
        inst = i.pop(0)
        i.append(inst)
        current_node = nodes[current_node][inst]
        total += 1
        if current_node.endswith("Z"):
            return total


for line in lines[2:]:
    match = re.match(map_regex, line)
    left, r1, r2 = match.groups()
    nodes[left] = (r1, r2)

part1 = get_map("AAA", instructions)
totals = [get_map(n, instructions) for n in nodes.keys() if n.endswith("A")]
part2 = lcm(*totals)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
