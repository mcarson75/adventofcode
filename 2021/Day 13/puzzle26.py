import numpy as np

fold = []
coord = set()

def do_fold(fold, axis, bef):
    aft = set()
    if axis == 'x':
        aft = set((x, y) if x < fold else (2*fold-x, y) for (x, y) in bef)
    else:
        aft = set((x, y) if y < fold else (x, 2*fold-y) for (x, y) in bef)

    return aft

for line in open("input.txt", 'r', encoding='utf-8'):
    l = line.strip()
    if not 'fold' in l and l !='':
        x, y = map(int, l.split(','))
        coord.add((x, y))
    elif 'fold' in l:
        _, _, inst = l.split()
        dir, num = inst.split('=')
        fold.append([dir, int(num)])

for axis, f in fold:
    coord = do_fold(f, axis, coord)

for y in range(max(y for _,y in coord)+1):
    for x in range(max(x for x, _ in coord)+1):
        print(' #'[(x,y) in coord], end='')
    print()