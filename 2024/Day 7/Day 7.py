from itertools import permutations, combinations

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def base(n, b, digits):
    if n == 0:
        return "0".zfill(digits)
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    return "".join(reversed(nums)).zfill(digits)


def check(total, nums, b):
    for i in range(b ** (len(nums) - 1)):
        pattern = base(i, b, len(nums) - 1)
        check = nums[0]
        for j in range(len(pattern)):
            if pattern[j] == "0":
                check *= nums[j + 1]
            elif pattern[j] == "1":
                check += nums[j + 1]
            elif pattern[j] == "2":
                check = int(str(check) + str(nums[j + 1]))
        if check == total:
            return total
    return 0


part1 = part2 = 0
for line in lines:
    a, b = line.split(": ")
    total = int(a)
    nums = [int(i) for i in b.split(" ")]
    valid = False

    part1 += (chk := check(total, nums, 2))
    if not chk:
        part2 += (chk := check(total, nums, 3))

print(f"Part 1: {part1}")
print(f"Part 2: {part1+part2}")
