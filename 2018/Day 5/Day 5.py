def reduce(poly):
    buf = []
    for p in poly:
        if buf and buf[-1] == p.swapcase():
            buf.pop()
        else:
            buf.append(p)
    return len(buf)


with open("input.txt", "r", encoding="utf-8") as f:
    polymer = f.read().strip()

agents = set([c.lower() for c in polymer])

part1 = reduce(polymer)
part2 = min([reduce(polymer.replace(a, "").replace(a.upper(), "")) for a in agents])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
