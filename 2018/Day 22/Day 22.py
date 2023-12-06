lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

for line in lines:
    type, value = line.split(":")
    if type == "depth":
        depth = int(value)
    elif type == "target":
        x, y = [int(n) for n in value.split(",")]
        target = x + y * 1j

erosions = {}
risks = {}


def geologic_index(coor, target):
    if coor == 0 or coor == target:
        return 0
    if coor.imag == 0:
        return int(coor.real) * 16807
    if coor.real == 0:
        return int(coor.imag) * 48271
    if coor - 1 and coor - 1j in erosions:
        return erosions[coor - 1] * erosions[coor - 1j]
    else:
        return None


def erosion(coor):
    return (geologic_index(coor, target) + depth) % 20183


def risk(coor):
    return erosion(coor) % 3


for x in range(int(target.real) + 1):
    for y in range(int(target.imag) + 1):
        erosions[x + y * 1j] = erosion(x + y * 1j)
        risks[x + y * 1j] = risk(x + y * 1j)

print(f"Part 1: {sum(risks.values())}")
