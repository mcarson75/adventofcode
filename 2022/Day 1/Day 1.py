calories = [0]

for line in open("input.txt", "r", encoding="utf-8"):
    if line.strip().isnumeric():
        calories[-1] += int(line)
    else:
        calories.append(0)

calories.sort(reverse=True)
print(f"Part 1: {calories[0]}")
print(f"Part 2: {sum(calories[0:3])}")