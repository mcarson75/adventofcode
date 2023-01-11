recipes = "768071"

scores = "37"
elf1 = 0
elf2 = 1

while recipes not in scores[-7:]:
    scores += str((e1 := int(scores[elf1])) + (e2 := int(scores[elf2])))
    elf1 = (elf1 + 1 + e1) % len(scores)
    elf2 = (elf2 + 1 + e2) % len(scores)

print(f"Part 1: {scores[int(recipes) : int(recipes) + 10]}")
print(f"Part 2: {scores.index(recipes)}")
