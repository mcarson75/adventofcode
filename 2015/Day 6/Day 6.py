import numpy as np
import re

with open("input.txt", 'r', encoding='utf-8') as f:
    strings = [s.rstrip() for s in f.readlines()]

houses_part1 = np.full((1000, 1000), False)
houses_part2 = np.full((1000, 1000), 0)
states_part2 = {'turn on': 1, 'turn off': -1, 'toggle': 2}

def switch(sl, state):
    states_part1 = {'turn on': True, 'turn off': False, 'toggle': np.invert(houses_part1[sl])}
    houses_part1[sl] = states_part1[state]
    houses_part2[sl] += states_part2[state]
    houses_part2[sl] = np.where(houses_part2[sl] < 0, 0, houses_part2[sl])

pattern = r'(turn on|turn off|toggle) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})'

for s in strings:
    match = re.search(pattern, s)
    x1, y1, x2, y2 = [int(match[x]) for x in range(2, 6)]
    sl = np.index_exp[x1:x2 +1, y1:y2 + 1]
    switch(sl, match[1])
    
print("Part 1: " + str(np.count_nonzero(houses_part1)))
print("Part 2: " + str(np.sum(houses_part2)))