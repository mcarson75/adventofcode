import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

letters = {x + y * 1j: grid[y, x] for (y, x) in np.argwhere(grid)}

part1 = 0
directions = [1, -1, 1j, -1j, 1 - 1j, 1 + 1j, -1 - 1j, -1 + 1j]
search = "XMAS"

for letter in letters:
    for dir in directions:
        found = True
        for i in range(len(search)):
            if (
                not letter + i * dir in letters
                or not letters[letter + i * dir] == search[i]
            ):
                found = False
                break
        if found:
            part1 += 1

part2 = 0
directions = [1 - 1j, 1 + 1j, -1 + 1j, -1 - 1j]
checks = ["SSMM", "SMMS", "MMSS", "MSSM"]

for letter in letters:
    if letters[letter] == "A":
        check = []
        for dir in directions:
            if letter + dir in letters:
                check.append(letters[letter + dir])
            else:
                break
        # if len(check) == 4:
        #     print("stop")
        if "".join(check) in checks:
            part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
