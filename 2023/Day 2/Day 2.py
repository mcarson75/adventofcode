lines = [
    l.strip().split(": ") for l in open("input.txt", "r", encoding="utf-8").readlines()
]

limits = {"red": 12, "green": 13, "blue": 14}
part1, part2 = 0, 0

for id, draws in lines:
    id = int(id[5:])
    power = {"red": 0, "green": 0, "blue": 0}

    draws = [draw.split() for draw in draws.replace(";", ",").split(", ")]
    draws = [[color, int(num)] for num, color in draws]
    for color in power.keys():
        power[color] = max([num for c, num in draws if c == color])

    if all([power[color] <= limits[color] for color in power.keys()]):
        part1 += id
    part2 += power["red"] * power["green"] * power["blue"]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
