from itertools import combinations

nums = [int(l.strip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]

part1 = None
for num in nums:
    sums = [num + n for n in nums]
    if 2020 in sums:
        part1 = num * (2020 - num)
        break

for comb in combinations(nums, 2):
    if sum(comb) < 2020:
        sums = [sum(comb) + n for n in nums]
        if 2020 in sums:
            part2 = comb[0] * comb[1] * (2020 - comb[0] - comb[1])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
