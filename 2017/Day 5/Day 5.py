c = [int(x) for x in open('input.txt', 'r', encoding='utf-8')]

pos = 0
steps = 0
while pos < len(c):
    next_pos = pos + c[pos]
    c[pos] += 1
    pos = next_pos
    steps += 1

print("Part 1: " + str(steps))

c = [int(x) for x in open('input.txt', 'r', encoding='utf-8')]

pos = 0
steps = 0
while pos < len(c):
    next_pos = pos + c[pos]
    c[pos] += 1 if c[pos] < 3 else -1
    pos = next_pos
    steps += 1

print("Part 2: " + str(steps))