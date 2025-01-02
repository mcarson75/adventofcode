input = [
    int(i)
    for i in [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()][
        0
    ]
]

pattern = [0, 1, 0, -1]
rep_pattern = lambda n: [x for xs in [[i] * n for i in pattern] for x in xs]


def do_transform(num):
    output = []
    for n in range(len(num)):
        ipattern = rep_pattern(n + 1)
        ipattern *= len(num) // len(ipattern) + 1
        ipattern = ipattern[1:]
        output.append(abs(sum([num[i] * ipattern[i] for i in range(len(num))])) % 10)
    return output


def do_part1(input, reps):
    for n in range(reps):
        input = do_transform(input)

    return "".join((str(i) for i in input))[:8]


part1 = do_part1(input, 100)

print(f"Part 1: {part1}")

offset = int("".join((str(i) for i in input[:7])))

input *= 10000
input = input[offset:]

for _ in range(100):
    sum = 0
    for i in range(len(input) - 1, -1, -1):
        sum += input[i]
        input[i] = sum % 10

part2 = "".join((str(i) for i in input))[:8]

print(f"Part 2: {part2}")
