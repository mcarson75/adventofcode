import re

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


class Particle:
    def __init__(self, pva):
        self.p = pva[:3]
        self.v = pva[3:6]
        self.a = pva[6:]

    def step(self):
        self.v = [self.v[i] + self.a[i] for i in range(3)]
        self.p = [self.p[i] + self.v[i] for i in range(3)]

    def dist(self):
        return sum([abs(x) for x in self.p])


particles = []
for l in lines:
    particles.append(Particle([int(i) for i in re.findall(r"[-\d]+", l)]))

remaining_particles = [p for p in particles]

for _ in range(1000):
    for p in particles:
        p.step()

    all_pos = [p.p for p in remaining_particles]
    remaining_particles = [p for p in remaining_particles if all_pos.count(p.p) == 1]


dist = [p.dist() for p in particles]
part1 = dist.index(min(dist))
part2 = len(remaining_particles)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
