import numpy as np

with open("input.txt", 'r', encoding='utf-8') as f:
    movement = list(f.read())
    
movement = np.array(list(map(lambda s: 1 if s=='(' else -1, movement)))
floor = np.cumsum(movement)

basement = np.where(floor < 0)[0] + 1
    
print(basement[0])