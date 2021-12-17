triangles = 0
lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]


for l in lines:
    t = [int(t) for t in l.split()]
    if sum(t[:2]) > t[2] and sum(t[1:]) > t[0] and (t[0] + t[2]) > t[1]:
        triangles += 1

print(triangles)