from collections import deque

moves = 355

array = deque([0])

for m in range(2017):
    array.rotate(-moves)
    array.append(m + 1)

print(f"Part 1: {array[0]}")

pos = 0
for m in range(50000000):
    new = (pos + moves) % (m + 1) + 1
    if new == 1:
        part2 = m + 1
    pos = new

print(f"Part 2: {part2}")
