import numpy as np

instr = []
coord = []

for line in open("input.txt", 'r', encoding='utf-8'):
    l = line.strip()
    if not 'fold' in l and l !='':
        x, y = map(int, l.split(','))
        coord.append([x, y])
    elif 'fold' in l:
        _, _, inst = l.split()
        dir, num = inst.split('=')
        instr.append([dir, int(num)])

max_x = max([c[1] for c in coord]) + 1
max_y = max([c[0] for c in coord]) + 1

total = 0
fold = instr[0][1]

matrix = np.zeros((fold, max_y))

for c in coord:
    x, y = c
    if x > fold:
        matrix[fold - x][y] =  matrix[fold - x][y] or 1
    else:
        matrix[x][y] = matrix[x][y] or 1
           
print(np.sum(matrix))