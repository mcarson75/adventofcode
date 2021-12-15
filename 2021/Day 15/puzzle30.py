import numpy as np

inr = lambda pos, arr: pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))
expand = lambda a, n: np.array([[x-9 if x>=10 else x for x in row] for row in np.add(a, n)])

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
base = np.array([[int(x) for x in l] for l in lines])

matrix = None
for y in range(5):
    new = np.concatenate((expand(base, y), expand(base, y+1), expand(base, y+2), expand(base, y+3), expand(base, y+4)), axis = 1)
    if matrix is None:
        matrix = new
    else:
        matrix = np.concatenate((matrix, new), axis=0)

q=[(0,0,0)]
costs = {}
while True:
    cost, x, y = q[0]
    if x==len(matrix)-1 and y == len(matrix[0]) -1:
        print(cost)
        break
    q=q[1:]
    for _x, _y in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
        if inr((_x, _y), matrix):
            nc = cost + matrix[_x][_y]
            if (_x, _y) in costs and costs[(_x, _y)] <= nc:
                continue
            costs[(_x, _y)] = nc
            q.append((nc, _x, _y))
    q=sorted(q)