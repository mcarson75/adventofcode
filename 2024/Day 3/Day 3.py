import re
from math import prod

line = "".join(
    [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
)


def mul_sum(line):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum([prod(int(a) for a in i) for i in re.findall(pattern, line)])


part1 = mul_sum(line)
part2 = sum([mul_sum(e.split("don't()")[0]) for e in line.split("do()")])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
