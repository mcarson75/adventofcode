# from copy import deepcopy

neighbors = lambda x, y, l: sum((i, j) in l for i in (x-1, x, x+1) for j in (y-1, y, y+1) if (i, j) != (x, y))
activate_lights = lambda l: {(x, y) for x in range(100) for y in range(100) 
                        if (x, y) in l and 2 <= neighbors(x, y, l) <= 3
                        or (x, y) not in l and neighbors(x, y, l) == 3}

corners = {(0, 0), (0, 99), (99, 0), (99, 99)}
reps = 100

with open("input.txt", 'r', encoding='utf-8') as f:
    lights1 = {(x,y) for y, line in enumerate(f) for x, char in enumerate(line.strip()) if char == '#'}

lights2 = corners | lights1.copy()

for n in range(reps):
    lights1 = activate_lights(lights1)
    lights2 = corners | activate_lights(lights2)
    
print("Part 1: " + str(len(lights1)))
print("Part 2: " + str(len(lights2)))