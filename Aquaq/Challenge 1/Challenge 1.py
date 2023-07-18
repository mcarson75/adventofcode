line = list(
    [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()][0]
)

hex_characters = "0123456789abcdef"

for n in range(len(line)):
    if line[n] not in hex_characters:
        line[n] = "0"

if len(line) % 3 != 0:
    new_length = (len(line) // 3 + 1) * 3
else:
    new_length = len(line)

result = "".join(
    line[:2]
    + line[new_length // 3 : new_length // 3 + 2]
    + line[new_length // 3 * 2 : new_length // 3 * 2 + 2]
)

print(f"Answer: {result}")
