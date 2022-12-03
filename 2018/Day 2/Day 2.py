from itertools import combinations

with open("input.txt", "r", encoding="utf-8") as f:
    boxes = [l.strip() for l in f.readlines()]


def check(s, num):
    char = {}
    for c in s:
        char[c] = char.get(c, 0) + 1

    return num in char.values()


count = [0, 0]

for b in boxes:
    count[0] += int(check(b, 2))
    count[1] += int(check(b, 3))

for i, j in combinations(boxes, 2):
    diff = [i[n] == j[n] for n in range(len(i))]
    if diff.count(False) == 1:
        part2 = i[: diff.index(False)] + i[diff.index(False) + 1 :]

print(f"Part 1: {(count[0]*count[1])}")
print(f"Part 2: {''.join(part2)}")
