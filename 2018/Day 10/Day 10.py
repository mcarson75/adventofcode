import re

input = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

pos = []
rectangle = lambda pos: max(p[0].imag for p in pos) - min(p[0].imag for p in pos)

for line in input:
    x, y, dx, dy = map(int, re.findall("-?\d+", line))
    pos.append((x + y * 1j, dx + dy * 1j))

min_size = rectangle(pos)
time = 0
pos = [(p[0] + (time := 10000) * p[1], p[1]) for p in pos]
while True:
    pos = [(p[0] + p[1], p[1]) for p in pos]
    min_size = min(min_size, size := rectangle(pos))
    time += 1
    if size != min_size:
        pos = [(p[0] - p[1], p[1]) for p in pos]
        time -= 1
        break

BLOCK = "\u2588"

pos = [p[0] for p in pos]
pos.sort(key=lambda p: p.imag)
min_y, max_y = map(int, [pos[i].imag for i in [0, -1]])

pos.sort(key=lambda p: p.real)
min_x, max_x = map(int, [pos[i].real for i in [0, -1]])

print("Part 1:")
for y in range(min_y, max_y + 1):
    pixels = "".join(
        [BLOCK if x + y * 1j in pos else " " for x in range(min_x, max_x + 1)]
    )
    print(pixels)

print(f"Part 2: {time}")
