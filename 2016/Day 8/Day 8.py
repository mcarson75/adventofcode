import numpy as np

screen = np.full((6, 50), ' ')
lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

for l in lines:
    if 'rect' in l:
        _, sh = l.split()
        x, y = map(int, sh.split('x'))
        screen[:y, :x] = '#'
    elif 'row' in l:
        _, _, row, _, num = l.split()
        row = int(row[2:])
        num = int(num)
        screen[row] = np.roll(screen[row], num)
    elif 'col' in l:
        _, _, col, _, num = l.split()
        col = int(col[2:])
        num = int(num)
        screen[:,col] = np.roll(screen[:,col], num)

print("Part 1: " + str(np.count_nonzero(screen=='#')))
print("Part 2:")
for l in screen:
    print(''.join(l))