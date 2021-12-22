with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f.readlines()]
    
pts = set()

def set_pts(x1, x2, y1, y2, z1, z2, state='on'):
    for x in range(x1, x2 + 1):
        if x not in range(-50, 51): break
        for y in range(y1, y2 + 1):
            if y not in range(-50, 51): break
            for z in range(z1, z2 + 1):
                if z not in range(-50, 51):
                    break
                if state == 'on':
                    pts.add((x, y, z))
                elif (x, y, z) in pts:
                    pts.remove((x, y, z))
                    
for l in lines:
    state, rem = l.split(" ")
    xa, ya, za = rem.split(",")
    _, x = xa.split("=")
    x1, x2 = map(int, x.split('..'))
    _, y = ya.split("=")
    y1, y2 = map(int, y.split('..'))
    _, z = za.split("=")
    z1, z2 = map(int, z.split('..'))
    set_pts(x1, x2, y1, y2, z1, z2, state)
    
print(len(pts))