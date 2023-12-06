from math import sqrt, ceil

lines = [l.strip().split(":")[1] for l in open("input.txt", "r")]


def getRB(time, dist):
    t = ceil((time - sqrt(time**2 - 4 * dist)) / 2)
    return time + 1 - 2 * t


times = [int(i) for i in lines[0].split()]
dists = [int(i) for i in lines[1].split()]
part1 = 1

for i in range(len(times)):
    time, dist = times[i], dists[i]
    part1 *= getRB(time, dist)

time = int(lines[0].replace(" ", ""))
dist = int(lines[1].replace(" ", ""))
part2 = getRB(time, dist)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
