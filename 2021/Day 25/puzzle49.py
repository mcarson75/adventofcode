matrix = []

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f.readlines()]
    
for l in lines:
    matrix.append(list(l))

max_x = len(matrix[0]) - 1
max_y = len(matrix) - 1
set_right = set()
set_down = set()

for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == '>':
            set_right.add((x, y))
        elif matrix[y][x] == 'v':
            set_down.add((x, y))

steps = 0
while True:
    steps += 1
    movement = False
    new_right = set()
    for r in set_right:
        x, y = r[0], r[1]
        next_x = x + 1 if x < max_x else 0
        if ((next_x, y)) not in set_right and ((next_x, y)) not in set_down:
            movement = True
            new_right.add((next_x, y))
        else:
            new_right.add((x, y))
    set_right = new_right

    new_down = set()
    for r in set_down:
        x, y = r[0], r[1]
        next_y = y + 1 if y < max_y else 0
        if ((x, next_y)) not in set_right and ((x, next_y)) not in set_down:
            movement = True
            new_down.add((x, next_y))
        else:
            new_down.add((x, y))
    set_down = new_down
    
    if not movement: break

print(steps)