import re

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

bags_string = r"\d ([a-z]+ [a-z]+) bags?(?:,|\.)"
bags_string_qt = r"(\d) ([a-z]+ [a-z]+) bags?(?:,|\.)"


def get_holders(color):
    if color in bags:
        holders = set(bags[color])
        for h in list(holders):
            holders |= get_holders(h)
        return holders
    else:
        return set()


def get_held(color, qty=1):
    if color in bags_part2:
        total = 0
        for h in bags_part2[color]:
            total += h[1] * (get_held(h[0], h[1]) + 1)
        return total
    else:
        return 0


bags = {}
bags_part2 = {}
for line in lines:
    parent, child = line.split(" bags contain ")
    children = re.findall(bags_string, child)
    parents = re.findall(bags_string_qt, child)
    for c in children:
        if c not in bags:
            bags[c] = [parent]
        else:
            bags[c].append(parent)

    for p in parents:
        qty, par = int(p[0]), p[1]
        if parent not in bags_part2:
            bags_part2[parent] = [(par, qty)]
        else:
            bags_part2[parent].append((par, qty))

part1 = get_holders("shiny gold")
part2 = get_held("shiny gold")

print(f"Part 1: {len(part1)}")
print(f"Part 2: {part2}")
