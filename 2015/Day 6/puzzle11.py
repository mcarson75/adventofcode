import numpy as np
import re

def switch(x1, y1, x2, y2, state):
    for x in range(min(x1,x2), max(x1,x2)+1):
        for y in range(min(y1,y2), max(y1,y2)+1):
            if state == 1:
                houses[x][y] = True
            elif state == 0:
                houses[x][y] = False
            elif state == -1:
                houses[x][y] = not houses[x][y]

with open("input.txt", 'r', encoding='utf-8') as f:
    strings = [s.rstrip() for s in f.readlines()]

houses = np.full((1000, 1000), False)
pattern = r'(turn on|turn off|toggle) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})'

for s in strings:
    match = re.search(pattern, s)
    if match.group(1) == 'turn on':
        state = 1
    elif match.group(1) == 'turn off':
        state = 0
    elif match.group(1) == 'toggle':
        state = -1
    x1 = int(match.group(2))
    y1 = int(match.group(3))
    x2 = int(match.group(4))
    y2 = int(match.group(5))
    switch(x1, y1, x2, y2, state)
    
print(np.count_nonzero(houses))