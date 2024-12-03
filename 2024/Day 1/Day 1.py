lines = [
    [int(i) for i in l.strip().split()]
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]

left = sorted([l[0] for l in lines])
right = sorted([l[1] for l in lines])

part1 = sum([abs(left[i] - right[i]) for i in range(len(left))])
part2 = sum([left[i] * right.count(left[i]) for i in range(len(left))])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
