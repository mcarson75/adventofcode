import re

def manhattan(pos1, pos2): return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

pattern = r'/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+)\s+(?P<size>\d+)T\s+(?P<used>\d+)T\s+(?P<available>\d+)T\s+(?P<use_percent>\d+)%'

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
nodes = []
viable = set()

for l in lines[2:]:
    match = re.search(pattern, l).groupdict()
    match = {k: int(v) for k, v in match.items()}
    
    nodes.append(match)

for node in nodes:
    if node["used"] == 0:
        continue
    poss = [n for n in nodes if n["available"] > node["used"]]
    this = (node["x"], node["y"])
    for p in poss:
        that = (p["x"], p["y"])
        if (that, this) not in viable and this != that:
            viable.add((this, that))
                   
part1 = len(viable)

goal = (max([n["x"] for n in nodes if n["y"] == 0]), 0)

hole = [(n["x"], n["y"]) for n in nodes if n["used"] == 0][0]
walls = [(n["x"], n["y"]) for n in nodes if n["size"] > 500]
# involved some manual intervention - this would be different if the walls were differently oriented
wall_open = ((walls[0][0] - 1, walls[0][1]))

part2 = 5 * (manhattan(goal, (0,0)) - 1) + manhattan(hole, wall_open) + manhattan(wall_open, goal)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))