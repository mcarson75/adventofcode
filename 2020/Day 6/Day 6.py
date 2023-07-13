lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
lines.append("")

part1 = 0
part2 = 0
group_any = set()
group_all = set()
new_group = True

for line in lines:
    if line:
        group_any |= set(list(line))
        if new_group:
            group_all |= set(list(line))
            new_group = False
        else:
            group_all &= set(list(line))
    else:
        part1 += len(group_any)
        part2 += len(group_all)
        group_any = set()
        group_all = set()
        new_group = True

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
