moves = [l.strip().split(',') for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

shifts = {'n': (0, -1, 1),
          's': (0, 1, -1),
          'ne': (1, -1, 0),
          'sw': (-1, 1, 0),
          'se': (1, 0, -1),
          'nw': (-1, 0, 1)}

def dist_from_zero(pos): return max([abs(i) for i in pos])

def do_shift(a, b): return tuple([sum(x) for x in zip(a, b)])

part2 = 0
pos = (0, 0, 0)
for m in moves:
    pos = do_shift(pos, shifts[m])
    part2 = max(part2, dist_from_zero(pos))

part1 = dist_from_zero(pos)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))