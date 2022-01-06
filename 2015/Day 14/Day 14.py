import numpy as np
import re

total = []
time = 2503
pattern = r'\S+ can fly (?P<speed>\d+) km/s for (?P<fly_time>\d+) seconds, but then must rest for (?P<rest_time>\d+) seconds.'

column_max = lambda c: np.array([1 if s==max(c) else 0 for s in c ])

lines = open("input.txt", 'r', encoding='utf-8').readlines()
     
def total_dist(s, f, r):
    base = np.array([s * min(t, f) for t in range(1, f + r + 1)])
    dist = np.array([])
    for n in range(int(time/(f+r))+1):
        dist = np.append(dist, base + n*base[-1])
    dist = dist[:time]
    
    return dist
    
for l in lines:
    match = re.match(pattern, l).groupdict()
    total.append([total_dist(int(match['speed']), int(match['fly_time']), int(match['rest_time']))])
    
total = np.array(total)

part1 = int(np.max(total))
part2 = np.max(np.sum(np.where(total==np.max(total, axis=0), 1, 0), axis=2))

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))