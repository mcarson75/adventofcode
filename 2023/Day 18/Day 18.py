lines = [
    l.strip().split() for l in open("input.txt", "r", encoding="utf-8").readlines()
]


class Vertices:
    move = lambda self, d, n, x, y: {
        "R": (x + n, y),
        "L": (x - n, y),
        "U": (x, y - n),
        "D": (x, y + n),
    }[d]

    def __init__(self):
        self.pos = (0, 0)
        self.length = 0
        self.total_area = 0

    def add_point(self, dir, length):
        new_pos = self.move(dir, length, *self.pos)
        self.length += length
        self.total_area += self.pos[0] * new_pos[1] - new_pos[0] * self.pos[1]
        self.pos = new_pos

    @property
    def area(self):
        return abs(self.total_area) // 2 + self.length // 2 + 1


Vertices1, Vertices2 = Vertices(), Vertices()
dir_map = {"0": "R", "1": "D", "2": "L", "3": "U"}

for dir, length, color in lines:
    Vertices1.add_point(dir, int(length))
    Vertices2.add_point(dir_map[color[-2]], int(color[2:-2], 16))

print(f"Part 1: {Vertices1.area}")
print(f"Part 2: {Vertices2.area}")
