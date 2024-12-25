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

tiles, _ = intcode.computer(code).run(0)

print(f"Part 1: {len([t for t in tiles if tiles[t]==2])}")

_, score = intcode.computer(code).run(0, freeplay=True)

print(f"Part 2: {score}")
