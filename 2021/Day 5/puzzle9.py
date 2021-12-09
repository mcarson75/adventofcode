import re
import numpy as np

pattern = r"(\d{1,3}),(\d{1,3}) -> (\d{1,3}),(\d{1,3})"

grid = np.zeros((1000,1000))

def line_fill(coord):
    x1 = coord[0]
    y1 = coord[1]
    x2 = coord[2]
    y2 = coord[3]
    
    if x1 == x2:
        for n in range(min(y1,y2), max(y1,y2)+1):
            grid[x1][n] += 1
    elif y1 == y2:
        for n in range(min(x1,x2), max(x1,x2)+1):
            grid[n][y1] += 1

with open('input.txt', 'r', encoding='utf-8') as read_file:
    lines = read_file.readlines()

for line in lines:
    groups = re.search(pattern, line)
    line_fill([int(x) for x in list(groups.groups(1))])


print(np.count_nonzero(grid>1))
