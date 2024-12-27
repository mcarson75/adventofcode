from math import ceil

lines = [
    l.strip().split(" => ")
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]


reactions = {}
distance = {"ORE": 0}
for line in lines:
    outq, oute = line[1].split(" ")
    reactions[oute] = {
        "quantity": int(outq),
        "ingredients": {
            chem[1]: int(chem[0])
            for chem in [item.split() for item in line[0].split(", ")]
        },
    }

materials = {m for m in reactions}
while len(distance) < len(materials):
    for material in materials:
        if material in distance:
            continue
        if not all([i in distance for i in reactions[material]["ingredients"]]):
            continue
        distance[material] = (
            max([distance[i] for i in reactions[material]["ingredients"]]) + 1
        )


def required_ore(fuel):
    global materials, reactions, distance
    needed = {"FUEL": fuel}
    while len(needed) > 1 or "ORE" not in needed:
        material = max(needed, key=lambda x: distance[x])
        quantity = needed[material]
        del needed[material]
        base_quantity, ingredients = reactions[material].values()
        for a, b in ingredients.items():
            if a not in needed:
                needed[a] = 0
            needed[a] += ceil(quantity / base_quantity) * b
    return needed["ORE"]


def search_fuel_target(ore):
    one_unit = part1
    target = ore // one_unit
    used_ore = required_ore(target)
    while True:
        target += (ore - used_ore) // one_unit + 1
        used_ore = required_ore(target)
        if used_ore > ore:
            break
    return target - 1


part1 = required_ore(1)
part2 = search_fuel_target(1000000000000)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
