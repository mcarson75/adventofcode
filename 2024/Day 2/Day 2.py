lines = [
    [int(i) for i in l.strip().split()]
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]


def check_safe(line):
    diffs = [line[i] - line[i + 1] for i in range(len(line) - 1)]
    return (all([i < 0 for i in diffs]) or all([i > 0 for i in diffs])) and all(
        [0 < abs(i) <= 3 for i in diffs]
    )


part1 = sum([check_safe(line) for line in lines])

part2 = 0
for line in lines:
    if check_safe(line):
        part2 += 1
    else:
        for i in range(len(line)):
            a = line[:]
            a.pop(i)
            if check_safe(a):
                part2 += 1
                break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
