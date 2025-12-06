batts = [
    [int(i) for i in l.strip()]
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]


def joltage(batt, size):
    joltage = ""
    for i in range(size, 0, -1):
        num = max(batt[: len(batt) - i + 1])
        joltage += str(num)
        batt = batt[batt.index(num) + 1 :]
    return int(joltage)


part1 = [joltage(b, 2) for b in batts]
part2 = [joltage(b, 12) for b in batts]

print(f"Part 1: {sum(part1)}")
print(f"Part 2: {sum(part2)}")
