import yaml

f = open("input.txt", "r", encoding="utf-8")
beg_state = f.readline().strip()[-2]
checksum = int(f.readline().strip().split()[-2])
input = yaml.safe_load(f)

states = {}
for s in input.keys():
    state = s.split()[-1][-1]
    states[state] = []
    for i in input[s].keys():
        commands = input[s][i]
        v = 1 if "1" in commands[0] else 0
        dir = 1 if "right" in commands[1] else -1
        nxt = commands[2].split()[-1][-2]
        states[state].append((v, dir, nxt))

state = states["A"]
pos = 0
array = set()

for _ in range(checksum):
    set, move, nxt = state[0 if pos not in array else 1]
    if set:
        array.add(pos)
    else:
        array.discard(pos)
    pos += move
    state = states[nxt]

print(f"Part 1: {len(array)}")
