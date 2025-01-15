import intcode

GRID = 50

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

code += [0] * 3000

part1 = 0
for x in range(GRID):
    for y in range(GRID):
        part1 += intcode.computer(code, [x, y]).get_beam()

print(f"Part 1: {part1}")


x = y = 0
while not intcode.computer(code, [x + 99, y]).get_beam():
    y += 1
    while not intcode.computer(code, [x, y + 99]).get_beam():
        x += 1

part2 = x * 10000 + y

print(f"Part 2: {part2}")
