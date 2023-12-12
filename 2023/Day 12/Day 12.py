lines = [
    l.strip().split() for l in open("input.txt", "r", encoding="utf-8").readlines()
]

pattern_cache = {}


def arrangements(springs, groups):
    arr_hash = hash(str(springs) + str(groups))
    if arr_hash in pattern_cache:
        return pattern_cache[arr_hash]

    if not groups:
        if not "#" in springs:
            return 1
        return 0

    count = 0
    for position in range(
        len(springs) - sum(groups[1:]) + len(groups[1:]) - groups[0] + 1
    ):
        possible = "." * position + "#" * groups[0] + "."

        for spring, possible_spring in zip(springs, possible):
            if spring != possible_spring and spring != "?":
                break
        else:
            count += arrangements(springs[len(possible) :], groups[1:])

    pattern_cache[arr_hash] = count
    return count


part1 = part2 = 0
for springs, group in lines:
    groups = [int(i) for i in group.split(",")]
    part1 += arrangements(springs, groups)
    part2 += arrangements("?".join((springs,) * 5), groups * 5)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
