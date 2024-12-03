import re
from math import prod

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def mul_sum(line):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum([prod(int(a) for a in i) for i in re.findall(pattern, line)])


part1 = sum([mul_sum(line) for line in lines])

enabled = "".join(lines).split("do()")
part2 = sum([mul_sum(e.split("don't()")[0]) for e in enabled])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
