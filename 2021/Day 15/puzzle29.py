import numpy as np

inr = lambda pos, arr: pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
matrix = np.array([[int(x) for x in l] for l in lines])

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