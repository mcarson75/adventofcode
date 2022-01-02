ring = lambda x: int((int((x - 1)**0.5) + 1) // 2)
manhattan = lambda x, y: abs(x) + abs(y)

input = 368078

# r = ring(input)
# r_dist = input - int((2 * r - 1)**2 + 1)

# x = r
# y = -(r-1)

# for n in range(r_dist):
#     if x == r and y < r:
#         y += 1
#     elif y == r and x > -r:
#         x -= 1
#     elif x == -r and y > -r:
#         y -= 1
#     elif y == -r and x < r:
#         x += 1

# print("Part 1: " + str(manhattan(x, y)))

part1 = False
part2 = False
r = 1
x = 1
y = 0
this = 2
points = {}
points[(0,0)] = 1
points2 = {}
points2[(0,0)] = 1

def sum_neighbors(x, y, p):
    t = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) in p:
                t += p[(i,j)]
    return t
    
while True:
    if not part1:
        points[(x, y)] = this
        if this == input:
            part1 = manhattan(x, y)
        this += 1

    if not part2:
        that = sum_neighbors(x, y, points2)
        if that > input:
            part2 = that
        else:
            points2[(x, y)] = that
        
    if part1 and part2:
        break
    
    if x == r and  -r < y < r:
        y += 1
    elif y == r and x > -r:
        x -= 1
    elif x == -r and y > -r:
        y -= 1
    elif y == -r and x <= r:
        x += 1
    if y == -r and x == r + 1:
        r += 1    

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
