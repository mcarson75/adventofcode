path_dist = lambda path: sum(paths[frozenset(x)] for x in zip(path, path[1:]))

from itertools import permutations as perm

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = (p.strip().split(" ")[::2] for p in f.readlines())
    paths = {frozenset(x[:2]): int(x[2]) for x in lines}
    dest = set.union(*(set(x) for x in paths.keys()))
    lengths = [path_dist(x) for x in perm(dest)]
    
print("Part 1: " + str(min(lengths)))
print("Part 2: " + str(max(lengths)))