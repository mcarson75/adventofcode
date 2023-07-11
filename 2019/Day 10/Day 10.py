import numpy as np
import math

grid = np.array(
    [list(l.rstrip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

asteroids = set(x + y * 1j for (y, x) in np.argwhere(grid == "#"))


def angle(start, end):
    result = math.atan2(end.real - start.real, start.imag - end.imag) * 180 / math.pi
    if result < 0:
        return result + 360
    return result


result = None
part1 = 0

for start in asteroids:
    cnt = len({angle(start, end) for end in asteroids if start != end})
    if cnt > part1:
        part1 = cnt
        result = start

asteroids.remove(result)

angles = sorted(
    ((angle(result, end), end) for end in asteroids),
    key=lambda x: (x[0], abs(result.real - x[1].real) + abs(result.imag - x[1].imag)),
)

index = 0
last = angles.pop(index)
last_angle = last[0]
cnt = 1

while cnt < 200 and angles:
    if index >= len(angles):
        index = 0
        last_angle = None
    if last_angle == angles[index][0]:
        index += 1
        continue
    last = angles.pop(index)
    last_angle = last[0]
    cnt += 1

print(f"Part 1: {part1}")
print(f"Part 2: {int(last[1].real * 100 + last[1].imag)}")
