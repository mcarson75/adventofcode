with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f.readlines()]

class cube:
    def __init__(self, x1, x2, y1, y2, z1, z2, state):
        self.x1, self.x2 = x1, x2
        self.y1, self.y2 = y1, y2
        self.z1, self.z2 = z1, z2
        self.state = state
        
    @property
    def volume(self):
        return self.state * abs(self.x2 - self.x1) * abs(self.y2 - self.y1) * abs(self.z2 - self.z1)

def overlap(this, that):
    return this.x2 > that.x1 and this.x1 < that.x2 and this.y2 > that.y1 and this.y1 < that.y2 and this.z2 > that.z1 and this.z1 < that.z2

cubes = []
for l in lines:
    state, rem = l.split(" ")
    state = 1 if state =='on' else 0
    x, y, z = rem.split(",")
    x1, x2 = map(int, x[2:].split('..'))
    y1, y2 = map(int, y[2:].split('..'))
    z1, z2 = map(int, z[2:].split('..'))
    
    this = cube(x1, x2 + 1, y1, y2 + 1, z1, z2 + 1, state)
    new_cubes = []
    for c in cubes:
        if overlap(this, c):
            new_state = -c.state
            x1_i, x2_i = max(this.x1, c.x1), min(this.x2, c.x2)
            y1_i, y2_i = max(this.y1, c.y1), min(this.y2, c.y2)
            z1_i, z2_i = max(this.z1, c.z1), min(this.z2, c.z2)
            new_cubes.append(cube(x1_i, x2_i, y1_i, y2_i, z1_i, z2_i, new_state))
    cubes.append(this)
    cubes.extend(new_cubes)
    
total = sum([c.volume for c in cubes])

print(total)