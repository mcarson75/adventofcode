lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

num_words = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "t3hree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "e8ight",
    "nine": "n9ine",
}

part1, part2 = 0, 0

for line in lines:
    part1 += int("".join([[i for i in line if i.isnumeric()][i] for i in [0, -1]]))

    for word, num in num_words.items():
        line = line.replace(word, num)

    part2 += int("".join([[i for i in line if i.isnumeric()][i] for i in [0, -1]]))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
