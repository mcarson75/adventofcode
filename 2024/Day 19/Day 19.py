from functools import cache

towels, patterns = [
    l for l in open("input.txt", "r", encoding="utf-8").read().split("\n\n")
]

towels = towels.split(", ")
patterns = patterns.splitlines()


@cache
def find_towels(pattern):
    counter = pattern in towels
    for towel in {t for t in towels if pattern.startswith(t)}:
        counter += find_towels(pattern[len(towel) :])
    return counter


all_found = [find_towels(pattern) for pattern in patterns]

part1 = len([a for a in all_found if a > 0])
part2 = sum(all_found)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
