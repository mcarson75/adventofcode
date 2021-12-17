input = []
triangles = 0
lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

for l in lines:
    input.append([int(t) for t in l.split()])

tri = []    
for y in range(0, len(input), 3):
    for x in range(3):
        tri.append([input[y][x], input[y+1][x], input[y+2][x]])
    
for t in tri:
    if sum(t[:2]) > t[2] and sum(t[1:]) > t[0] and (t[0] + t[2]) > t[1]:
        triangles += 1

print(triangles)