import numpy as np

with open("input.txt", 'r', encoding='utf-8') as f:
    movement = list(f.read())

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
    
part1 = np.count_nonzero(get_houses(movement))
part2 = np.count_nonzero(np.logical_or(get_houses(movement[::2]), get_houses(movement[1::2])))

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))