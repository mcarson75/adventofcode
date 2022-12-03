priority = [0, 0]


def char_pri(char):
    if char.islower():
        return ord(char) - ord("a") + 1
    else:
        return ord(char) - ord("A") + 27


with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

for line in lines:
    char = list(
        set.intersection(
            *[set(l) for l in [line[: len(line) // 2], line[len(line) // 2 :]]]
        )
    )[0]

    priority[0] += char_pri(char)

for n in range(0, len(lines) - 1, 3):
    char = list(set.intersection(*[set(l) for l in lines[n : n + 3]]))[0]

    priority[1] += char_pri(char)

print(f"Part 1: {priority[0]}")
print(f"Part 2: {priority[1]}")
