from itertools import permutations as perm

matrix = []

happiness = lambda path: sum(paths[frozenset(x)] for x in zip(path, path[1:]))

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l for l in f.read().split('\n')]
    
for l in lines:
    s, _, sign, num, _, _, _, _, _, _, t = l.split()    
    t.strip()
    t = t[0:-1]
    
    num = int(num)
    if sign == 'lose':
        num = -num
    
    matrix.append([s, t, num])

paths={}
for m in matrix:
    s = frozenset(m[:2])
    if not s in paths.keys():
        paths[s] = m[2]
    else:
        paths[s] += m[2]

people = set.union(*(set(x) for x in paths.keys()))
c = [list(c) for c in perm(people)]
for i in range(len(c)):
    c[i].append(c[i][0])    
total = [happiness(x) for x in c]

print(max(total))