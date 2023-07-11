lines = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip()
]

width = 25
height = 6

layers = []
while lines:
    layers.append(lines[: width * height])
    lines = lines[width * height :]

min_zeros = width * height
part1 = None
for layer in layers:
    if layer.count(0) < min_zeros:
        min_zeros = layer.count(0)
        part1 = layer.count(1) * layer.count(2)

final = []
for n in range(len(layers[0])):
    l = 0
    while layers[l][n] == 2:
        l += 1

    final.append(layers[l][n])

print(f"Part 1: {part1}")

BLOCK = "\u2588"
pixels = "".join([BLOCK if x == 1 else " " for i, x in enumerate(final)])

for e in range(width, len(final) + 1, width):
    print(pixels[e - width : e])
