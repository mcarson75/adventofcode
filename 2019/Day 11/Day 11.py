import intcode

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

code += [0] * 3000

pos = 0
dir = -1j
panels = dict()

tiles = intcode.computer(code).run(0)

print(f"Part 1: {len(tiles)}")
print("Part 2:\n")

tiles = intcode.computer(code).run(1)

xmax = int(max([t.real for t in tiles]))
ymax = int(max([t.imag for t in tiles]))

for y in range(ymax + 1):
    for x in range(xmax + 1):
        if complex(x, y) not in tiles:
            tiles[complex(x, y)] = 0
    t = "".join(["#" if tiles[complex(x, y)] == 1 else " " for x in range(xmax + 1)])
    print(f"{t}")
