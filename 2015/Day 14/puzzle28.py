import numpy as np

total = []
time = 2503
points = {}
dist = {}

column_max = lambda c: np.array([1 if s==max(c) else 0 for s in c ])

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l for l in f.read().split('\n')]

def total_dist(s, f, r):
    base = [s * min(t, f) for t in range(1, f + r + 1)]
    dist = []
    for n in range(int(time/(f+r))+1):
        dist.extend([x + n*base[-1] for x in base])
    
    dist = dist[:time]
    
    return dist
    
for l in lines:
    reindeer, _, _, speed, _, _, fly_time, _, _, _, _, _, _, rest_time, _ = l.split()
    dist[reindeer] = total_dist(int(speed), int(fly_time), int(rest_time))

matrix = np.array([dist[k] for k in dist.keys()])
points = np.full_like(matrix, 0)

for t in range(time):
    points[:,t] = column_max(matrix[:,t])

total_points = [sum(x) for x in points]

print(max(total_points))