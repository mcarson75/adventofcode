import numpy as np

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [[int(i) for i in list(l.strip())] for l in f.readlines()]

lines = np.array(lines)


def find_scenic(ht, array):
    bool_array = [n < ht for n in array]
    return all(bool_array) if len(bool_array) > 0 else True, bool_array.index(
        False
    ) + 1 if False in bool_array else len(bool_array)


part1 = 0
part2 = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        current = lines[i, j]

        west_visible, west_scenic = find_scenic(current, lines[i, :j][::-1])
        east_visible, east_scenic = find_scenic(current, lines[i, j + 1 :])
        north_visible, north_scenic = find_scenic(current, lines[:i, j][::-1])
        south_visible, south_scenic = find_scenic(current, lines[i + 1 :, j])

        part1 += any([west_visible, east_visible, north_visible, south_visible])
        part2 = max(part2, west_scenic * east_scenic * north_scenic * south_scenic)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
