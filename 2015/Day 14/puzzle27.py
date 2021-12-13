total = []
time = 2503

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l for l in f.read().split('\n')]

def total_dist(s, f, r):
    dist = (s * f) * int(time/(f+r))
    rem = time % (f+r)
    dist += min(rem, f) * s
    
    return dist
    
for l in lines:
    reindeer, _, _, speed, _, _, fly_time, _, _, _, _, _, _, rest_time, _ = l.split()
    total.append(total_dist(int(speed), int(fly_time), int(rest_time)))
    
print(max(total))