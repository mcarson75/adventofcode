from itertools import permutations as perm
from collections import defaultdict
import re

matrix = []
pattern = r'(\S+) would (gain|lose) (\d+) happiness units by sitting next to (\S+)\.'
paths = defaultdict()

happiness = lambda path: sum(paths[frozenset(x)] for x in zip(path, path[1:]))

def get_happiness(p):
    c = [list(c) for c in perm(p)]
    [x.append(x[0]) for x in c]
    return max([happiness(x) for x in c])

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
for l in lines:
    match = re.match(pattern, l)
    s, t = match[1], match[4]
    num = int(match[3]) if match[2] == 'gain' else -int(match[3])

    s = frozenset([s, t])
    if s in paths:
        paths[s] += num
    else:
        paths[s] = num


people = set.union(*(set(x) for x in paths.keys()))

for p in people:
    paths[frozenset(['me', p])] = 0

people_withme = set.union(*(set(x) for x in paths.keys()))

part1 = get_happiness(people)
part2 = get_happiness(people_withme)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))