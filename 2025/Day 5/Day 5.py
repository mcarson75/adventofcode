lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
range_ends = [[int(i) for i in line.split("-")] for line in lines if "-" in line]
ranges = [range(r[0], r[1] + 1) for r in range_ends]
ids = [int(line) for line in lines if line and "-" not in line]

part1 = len([id for id in ids if any([id in rge for rge in ranges])])

combined = set()
for old in ranges:
    merged = set([old])
    for new in combined:
        if old.stop >= new.start and new.stop >= old.start:
            merged.add(new)
    combined -= merged
    combined.add(range(min(m.start for m in merged), max(m.stop for m in merged)))

part2 = sum([len(r) for r in combined])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
