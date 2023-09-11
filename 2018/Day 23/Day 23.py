lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


class bot:
    def __init__(self, line):
        p, r = line.split(", ")
        self.range = int(r[2:])
        self.x, self.y, self.z = map(int, p[5:-1].split(","))

    def dist(self, other):
        if type(other) is bot:
            return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
        elif type(other) is tuple:
            return (
                abs(self.x - other[0]) + abs(self.y - other[1]) + abs(self.z - other[2])
            )

    def inrange(self, other):
        return self.dist(other) <= self.range


def max_overlap(xrange, yrange, zrange):
    max_overlap = 0
    max_pt = (None, None, None)
    for x in xrange:
        for y in yrange:
            for z in zrange:
                num = len([b for b in bots if b.inrange((x, y, z))])
                if num > max_overlap:
                    max_overlap = num
                    max_pt = (x, y, z)

    return max_pt


bots = []
for line in lines:
    bots.append(bot(line))

bots = sorted(bots, key=lambda r: r.range, reverse=True)
max_bot = bots[0]

in_range = [b for b in bots if max_bot.inrange(b)]

print(f"Part 1: {len(in_range)}")

xs = [b.x for b in bots]
ys = [b.y for b in bots]
zs = [b.z for b in bots]

min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)
min_z, max_z = min(zs), max(zs)

x_step = (max_x - min_x) // 50
y_step = (max_y - min_y) // 50
z_step = (max_z - min_z) // 50

xrange = range(min_x, max_x + x_step, x_step)
yrange = range(min_y, max_y + y_step, y_step)
zrange = range(min_z, max_z + z_step, z_step)

center = max_overlap(xrange, yrange, zrange)

while x_step > 1 and y_step > 1 and z_step > 1:
    x_step //= 10
    y_step //= 10
    z_step //= 10

    x_step = max(x_step, 1)
    y_step = max(y_step, 1)
    z_step = max(z_step, 1)

    xrange = range(-10 * x_step + center[0], 11 * x_step + center[0], x_step)
    yrange = range(-10 * y_step + center[1], 11 * y_step + center[1], y_step)
    zrange = range(-10 * z_step + center[2], 11 * z_step + center[2], z_step)

    center = max_overlap(xrange, yrange, zrange)


print(f"Part 2: {abs(center[0]) + abs(center[1]) + abs(center[2])}")
