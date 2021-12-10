import numpy as np

def get_houses(movement):
    houses = np.full([1000, 1000], False)

    x=500
    y=500
    houses[x, y] = True

    for m in movement:
        if m == "^":
            y += 1
        elif m == "v":
            y -= 1
        elif m == ">":
            x += 1
        elif m == "<":
            x -=1
        houses[x, y] = True
    
    return houses

with open("input.txt", 'r', encoding='utf-8') as f:
    movement = list(f.read())

houses = np.logical_or(get_houses(movement[::2]), get_houses(movement[1::2]))
    
print(np.count_nonzero(houses))