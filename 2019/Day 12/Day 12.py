import re
from math import lcm

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

STEPS = 1000


class moon:
    def __init__(self, code):
        self.pos = [int(i) for i in re.findall(r"-?\d+", code)]
        self.init_pos = self.pos[:]
        self.vel = [0, 0, 0]
        self.step = 0
        self.loop = [0, 0, 0]

    def __repr__(self):
        return f"pos=<x={self.pos[0]}, y={self.pos[1]}, z={self.pos[2]}>, vel=<x={self.vel[0]}, y={self.vel[1]}, z={self.vel[2]}>"

    def update_velocity(self):
        for moon in moons:
            for dim in range(3):
                if moon.pos[dim] < self.pos[dim]:
                    self.vel[dim] -= 1
                elif moon.pos[dim] > self.pos[dim]:
                    self.vel[dim] += 1

    def move(self):
        for dim in range(3):
            self.pos[dim] += self.vel[dim]
        self.step += 1
        for dim in range(3):
            if (
                self.loop[dim] == 0
                and self.pos[dim] == self.init_pos[dim]
                and self.vel[dim] == 0
            ):
                self.loop[dim] = self.step

    @property
    def energy(self):
        return sum(abs(p) for p in self.pos) * sum(abs(v) for v in self.vel)

    @property
    def loops(self):
        return all(l > 0 for l in self.loop)


moons = set(moon(line) for line in lines)

step = 0

while not all((m.loops for m in moons)):
    [moon.update_velocity() for moon in moons]
    [moon.move() for moon in moons]
    step += 1
    if step == STEPS:
        part1 = sum(moon.energy for moon in moons)

part2 = lcm(*[max([m.loop[n] for m in moons]) for n in range(3)])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
