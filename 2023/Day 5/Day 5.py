import re

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n\n")


def getNext(rs, source):
    for r in rs:
        if r[1] <= source < r[1] + r[2]:
            return r[0] - r[1] + source
    return source


def getNextRanges(maps, src):
    ranges, i = [], 0
    while True:
        tgt_min, src_min, spread = maps[i]
        if src_min > src[0]:
            if src_min > src[1]:
                ranges.append(src)
                return ranges
            ranges.append((src[0], src_min - 1))
            src = src_min, src[1]
        elif src_min <= src[0] < src_min + spread:
            offset = tgt_min - src_min
            if src[1] < src_min + spread:
                ranges.append(tuple(r + offset for r in src))
                return ranges
            ranges.append((src[0] + offset, tgt_min + spread))
            src = src_min + spread, src[1]
        elif src_min + spread <= src[0]:
            i += 1
            if i == len(maps):
                break
    ranges.append(src)
    return ranges


for line in lines:
    if "seeds" in line:
        seeds = list(map(int, re.findall("\d+", line)))
        source_range = [
            (seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
        ]
    else:
        target_ranges = list(map(int, re.findall("\d+", line)))
        target_ranges = sorted(
            [target_ranges[i : i + 3] for i in range(0, len(target_ranges), 3)],
            key=lambda x: x[1],
        )
        seeds = [getNext(target_ranges, s) for s in seeds]
        source_range = sum(
            (getNextRanges(target_ranges, src) for src in source_range), []
        )

part1 = min(seeds)
part2 = min([min(r) for r in source_range])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
