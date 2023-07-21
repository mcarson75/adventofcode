from collections import Counter

jolts = [int(l.strip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]

jolts.append(max(jolts) + 3)
jolts.append(0)
jolts.sort()

diffs = [j - i for i, j in zip(jolts[:-1], jolts[1:])]

part1 = diffs.count(1) * diffs.count(3)

jolts = jolts[1:]
counter = {0: 1}

for adapter in jolts:
    counter[adapter] = (
        counter.get(adapter - 3, 0)
        + counter.get(adapter - 2, 0)
        + counter.get(adapter - 1, 0)
    )

print(f"Part 1: {part1}")
print(f"Part 2: {counter[max(jolts)]}")
