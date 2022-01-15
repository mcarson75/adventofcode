ranges = [l.strip().split('-') for l in open("input.txt", 'r', encoding='utf-8').readlines()]
ranges = [[int(x) for x in l] for l in ranges]

ranges = sorted(ranges, key = lambda x: x[0])

part1 = 0
part2 = 0
low = 0
for r in ranges:
    if part1 in range(r[0], r[1] + 1):
        part1 = max(part1, r[1] + 1)
    
    if low not in range(r[0], r[1] + 1) and low < r[0]:
        part2 += r[0] - low
    low = max(low, r[1] + 1)

part2 += 4294967296 - low

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))