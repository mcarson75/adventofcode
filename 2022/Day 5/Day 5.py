import re

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.replace("\n", "") for l in f.readlines()]

crates = lines[: lines.index("")]
moves = lines[lines.index("") + 1 :]

crates_horiz = [c[1::4] for c in crates[:-1][::-1]]
crates1 = [
    "".join([c[i] for c in crates_horiz]).rstrip() for i in range(len(crates_horiz[0]))
]

crates2 = crates1.copy()

for move in moves:
    [num, start, end] = [int(i) for i in re.findall("\d+", move)]

    start -= 1
    end -= 1

    crates1[end] += crates1[start][-num:][::-1]
    crates1[start] = crates1[start][:-num]

    crates2[end] += crates2[start][-num:]
    crates2[start] = crates2[start][:-num]

part1 = "".join([c[-1] for c in crates1])
part2 = "".join([c[-1] for c in crates2])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
