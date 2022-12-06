with open("input.txt", "r", encoding="utf-8") as f:
    input = f.read().strip()


def find_unique(input, length):
    for n in range(length, len(input)):
        check = input[n - length : n]
        if len(set(check)) == length:
            return n


part1 = find_unique(input, 4)
part2 = find_unique(input, 14)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
