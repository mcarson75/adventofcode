lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

limits = {"red": 12, "green": 13, "blue": 14}
part1, part2 = 0, 0

for line in lines:
    id, draws = line.split(": ")
    _, id = id.split(" ")
    id = int(id)

    powers = {"red": 0, "green": 0, "blue": 0}

    subsets = draws.split("; ")
    for subset in subsets:
        balls = subset.split(", ")
        for ball in balls:
            num, color = ball.split(" ")
            num = int(num)

            powers[color] = max(num, powers[color])

    part2 += powers["red"] * powers["green"] * powers["blue"]
    if (
        powers["red"] <= limits["red"]
        and powers["green"] <= limits["green"]
        and powers["blue"] <= limits["blue"]
    ):
        part1 += id

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
