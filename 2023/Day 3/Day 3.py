import numpy as np

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)


def around(start, target):
    result = set()
    y, x = start
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (j, i) in target:
                result.add((j, i))
    return result


not_empty = set((y, x) for (y, x) in np.argwhere(grid != "."))
numerals = set((y, x) for (y, x) in np.argwhere(np.char.isnumeric(grid)))
gears = set((y, x) for (y, x) in np.argwhere(grid == "*"))
symbols = not_empty - numerals

gear_pos = {}
part1 = 0
part2 = 0

for num in sorted(list(numerals)):
    if num in numerals:
        is_part = around(num, symbols)
        is_gear = around(num, gears)
        numerals.remove(num)
        y, x = num
        this_num = grid[num]
        while (y, x + 1) in numerals:
            x += 1
            is_part |= around((y, x), symbols)
            is_gear |= around((y, x), gears)
            this_num += grid[(y, x)]
            numerals.remove((y, x))
        this_num = int(this_num)
        if is_part:
            part1 += this_num
        for gear in is_gear:
            if gear in gear_pos:
                gear_pos[gear].append(this_num)
            else:
                gear_pos[gear] = [this_num]

for gear in gear_pos:
    ratios = gear_pos[gear]
    if len(ratios) == 2:
        part2 += ratios[0] * ratios[1]


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
