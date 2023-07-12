passwords = [
    l.strip().split(": ") for l in open("input.txt", "r", encoding="utf-8").readlines()
]

part1 = 0
part2 = 0
for policy, pw in passwords:
    num, letter = policy.split(" ")
    min, max = [int(n) for n in num.split("-")]
    if min <= pw.count(letter) <= max:
        part1 += 1
    if [pw[i] for i in [min - 1, max - 1]].count(letter) == 1:
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
