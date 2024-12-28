import intcode

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

code += [0] * 3000

o2, freespace = intcode.computer(code).run()

pos = 0
q = [(0, pos)]
costs = {pos: 0}
while q:
    cost, pos = q.pop(0)
    if pos == o2:
        break
    for np in [pos + d for d in [-1j, 1j, -1, 1]]:
        nc = cost + 1
        if np in costs and nc >= costs[np]:
            continue
        if np not in freespace:
            continue
        costs[np] = nc
        q.append((nc, np))

part1 = cost
print(f"Part 1: {part1}")

filled = {o2}
freespace -= filled
part2 = 0
while freespace:
    filled |= freespace & set(f + d for f in filled for d in [-1j, 1j, -1, 1])
    freespace -= filled
    part2 += 1

print(f"Part 2: {part2}")
