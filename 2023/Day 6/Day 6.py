from math import sqrt, ceil, prod

lines = [l.strip().split(":")[1] for l in open("input.txt", "r")]


def getRB(data):
    time, dist = data
    t = ceil((time - sqrt(time**2 - 4 * dist)) / 2)
    return time + 1 - 2 * t


data = zip(*[[int(i) for i in l.split()] for l in lines])
data2 = [int(l.replace(" ", "")) for l in lines]
rb = [getRB(d) for d in data]

part1 = prod(rb)
part2 = getRB(data2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
