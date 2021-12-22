range_intersect = lambda r1, r2: range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f.readlines()]

class cube:
    def __init__(self, x, y, z, state):
        self.x, self.y, self.z = x, y, z
        self.state = state
        
    @property
    def volume(self):
        return self.state * len(self.x) * len(self.y) * len(self.z)

    def overlap(self, that):
        return range_intersect(self.x, that.x), range_intersect(self.y, that.y), range_intersect(self.z, that.z)

cubes = []
for l in lines:
    state, rem = l.split(" ")
    state = 1 if state =='on' else 0
    x, y, z = rem.split(",")
    x1, x2 = map(int, x[2:].split('..'))
    y1, y2 = map(int, y[2:].split('..'))
    z1, z2 = map(int, z[2:].split('..'))
    
    this = cube(range(x1, x2 + 1), range(y1, y2 +1), range(z1, z2 + 1), state)
    new_cubes = []
    for c in cubes:
        xi, yi, zi = this.overlap(c)
        if all([xi, yi, zi]):
            new_state = -c.state
            int_cube = cube(xi, yi, zi, new_state)
            new_cubes.append(int_cube)
    cubes.append(this)
    cubes.extend(new_cubes)
    
total = sum([c.volume for c in cubes])

print(total)