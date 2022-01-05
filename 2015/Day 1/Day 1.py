import numpy as np

with open("input.txt", 'r', encoding='utf-8') as f:
    text = f.read()
    floors = text.count('(') - text.count(')')

movement = np.array(list(map(lambda s: 1 if s=='(' else -1, text)))
floor = np.cumsum(movement)

basement = np.min(np.where(floor < 0)) + 1
    
print("Part 1: " + str(floors))
print("Part 2: " + str(basement))
