lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

allergens = {}
ingredients = set()
ing_count = {}

for line in lines:
    i, a = line[:-1].split(" (contains ")
    ing = set(i.split(" "))
    for i in ing:
        if i in ing_count:
            ing_count[i] += 1
        else:
            ing_count[i] = 1
    ingredients.update(ing)
    aller = a.split(", ")
    for a in aller:
        if a in allergens:
            allergens[a] &= ing
        else:
            allergens[a] = set(ing)

possibles = set()
for a in allergens:
    possibles.update(allergens[a])

non_allergens = ingredients - possibles
part1 = 0
for n in non_allergens:
    part1 += ing_count[n]

definitive = set()
while any([len(allergens[a]) > 1 for a in allergens]):
    for a in allergens:
        if len(allergens[a]) == 1:
            definitive.update(allergens[a])
        else:
            allergens[a] -= definitive

allergen_names = sorted(list(allergens.keys()))
part2 = ""
for a in allergen_names:
    part2 += allergens[a].pop() + ","

part2 = part2[:-1]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
