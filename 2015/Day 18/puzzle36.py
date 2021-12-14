import numpy as np

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
matrix = np.array([[True if c=='#' else False for c in list(l)] for l in lines])

def get_neighbors(x, y):
    global matrix
    
    x1 = max(0, x-1)
    x2 = min(x+1, len(matrix[0]))
    y1 = max(0, y-1)
    y2 = min(y+1, len(matrix))
    
    sub = matrix[y1:y2+1, x1:x2+1]
    
    return np.sum(sub) - matrix[y][x]

reps = 100

for _ in range(reps):
    new_matrix = np.full_like(matrix, False)
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            n = get_neighbors(x, y)
            if matrix[y][x] and n in [2, 3]:
                new_matrix[y][x] = True
            elif not matrix[y][x] and n == 3:
                new_matrix[y][x] = True
    matrix = new_matrix
    matrix[0][0] = True
    matrix[0][len(matrix[0]) - 1] = True
    matrix[len(matrix) - 1][0] = True
    matrix[len(matrix) - 1][len(matrix[0]) - 1] = True

print(np.sum(matrix))