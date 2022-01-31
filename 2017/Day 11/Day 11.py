moves = [l.strip().split(',') for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

def dist_from_zero(pos):
    return max([abs(i) for i in pos])

part2 = 0

pos = (0, 0, 0)
for m in moves:
    q, r, s = pos
    if m == 'n':
        s += 1
        r -= 1
    elif m == 's':
        s -= 1
        r += 1
    elif m == 'ne':
        q += 1
        r -= 1
    elif m == 'sw':
        q -= 1
        r += 1
    elif m == 'se':
        q += 1
        s -= 1
    elif m == 'nw':
        q -= 1
        s += 1
    pos = (q, r, s)
    part2 = max(part2, dist_from_zero(pos))

part1 = dist_from_zero(pos)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))