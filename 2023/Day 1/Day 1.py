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

values1, values2 = [], []

for line in lines:
    nums = [i for i in line if i.isnumeric()]
    values1.append(int(nums[0] + nums[-1]))

    for word, num in num_words.items():
        line = line.replace(word, num)

    nums = [i for i in line if i.isnumeric()]
    values2.append(int(nums[0] + nums[-1]))


part1 = sum(values1)
print(f"Part 1: {part1}")

part2 = sum(values2)
print(f"Part 1: {part2}")
