with open("input.txt", "r", encoding="utf-8") as f:
    input = f.read().strip()


def find_unique(input, l):
    for n in range(l, len(input)):
        if len(set(input[n - l : n])) == l:
            return n


print(f"Part 1: {find_unique(input, 4)}")
print(f"Part 2: {find_unique(input, 14)}")
