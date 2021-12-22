from copy import deepcopy

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f.readlines()]

class cube:
    def __init__(self, x1, x2, y1, y2, z1, z2, state):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        if isinstance(state, int):
            self.state = state
        else:
            self.state = int(state == 'on')
        
    @property
    def volume(self):
        return self.state * abs(self.x2 - self.x1) * abs(self.y2 - self.y1) * abs(self.z2 - self.z1)

def overlap(this, that):
    return this.x2 > that.x1 and this.x1 < that.x2 and this.y2 > that.y1 and this.y1 < that.y2 and this.z2 > that.z1 and this.z1 < that.z2

cubes = []
for l in lines:
    state, rem = l.split(" ")
    xa, ya, za = rem.split(",")
    _, x = xa.split("=")
    x1, x2 = map(int, x.split('..'))
    _, y = ya.split("=")
    y1, y2 = map(int, y.split('..'))
    _, z = za.split("=")
    z1, z2 = map(int, z.split('..'))
    
    x2, y2, z2 = x2 + 1, y2 + 1, z2 + 1
    
    new_cubes = []
    this = cube(x1, x2, y1, y2, z1, z2, state)
    for c in cubes:
        if overlap(this, c):
            if c.x1 < this.x1:
                new_cube = deepcopy(c)
                new_cube.x2 = this.x1
                c.x1 = this.x1
                new_cubes.append(new_cube)
            if c.x2 > this.x2:
                new_cube = deepcopy(c)
                new_cube.x1 = this.x2
                c.x2 = this.x2
                new_cubes.append(new_cube)
            if c.y1 < this.y1:
                new_cube = deepcopy(c)
                new_cube.y2 = this.y1
                c.y1 = this.y1
                new_cubes.append(new_cube)
            if c.y2 > this.y2:
                new_cube = deepcopy(c)
                new_cube.y1 = this.y2
                c.y2 = this.y2
                new_cubes.append(new_cube)
            if c.z1 < this.z1:
                new_cube = deepcopy(c)
                new_cube.z2 = this.z1
                c.z1 = this.z1
                new_cubes.append(new_cube)
            if c.z2 > this.z2:
                new_cube = deepcopy(c)
                new_cube.z1 = this.z2
                c.z2 = this.z2
                new_cubes.append(new_cube)
        else:
            new_cubes.append(c)
    
    new_cubes.append(this)

    cubes = new_cubes
            
total = sum([c.volume for c in cubes])

print(total)