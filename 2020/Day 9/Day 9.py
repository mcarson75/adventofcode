nums = [int(l.strip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]

part1 = None
part2 = None
for n in range(25, len(nums) + 1):
    valid = False
    num_list = nums[n - 25 : n]
    for num in num_list:
        if nums[n] - num in num_list:
            valid = True
    if not valid:
        part1 = nums[n]
        num_list = nums[:n]
        break

for length in range(3, len(num_list) + 1):
    for start in range(len(num_list) - length):
        if sum(num_list[start : start + length]) == part1:
            region = num_list[start : start + length]
            part2 = min(region) + max(region)
            break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
