lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

pipes = {}

for line in lines:
    l, r = line.split(' <-> ')
    pipes[int(l)] = [int(x) for x in r.split(', ')]

def get_connected(node, nodes):
    for n in pipes[node]:
        if not n in nodes:
            nodes.add(n)
            get_connected(n, nodes)
    return nodes

nodes = get_connected(0, set())
part1 = len(nodes)

groups = []
for k in pipes.keys():
    if not any([k in g for g in groups]):
        groups.append(get_connected(k, set()))

part2 = len(groups)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))