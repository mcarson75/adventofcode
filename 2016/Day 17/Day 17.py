from hashlib import md5
from collections import deque
from itertools import compress

input = 'mmsxrhfx'
    
def get_doors(path):
    hash = md5(str.encode(input + path)).hexdigest()
    return [int(c, 16) > 10 for c in hash[:4]]

def get_next_room(pos):
    out = []
    row, col = pos
    out.append((row - 1, col) if row - 1 in range(4) else None)
    out.append((row + 1, col) if row + 1 in range(4) else None)
    out.append((row, col - 1) if col - 1 in range(4) else None)
    out.append((row, col + 1) if col + 1 in range(4) else None)

    return out

def next_states(state):
    pos, path = state
    dirs = 'UDLR'
    doors = get_doors(path)
    next_pos = get_next_room(pos)
    
    for d in compress(zip(dirs, next_pos), [all(i) for i in zip(doors, next_pos)]):
        yield(d[1], path + d[0])

def get_paths():
    seen = set()
    queue = deque([((0, 0), '')]) # (row, col), path to get here
    valid = []
    
    while queue:
        state = queue.popleft()
        pos, path = state
        
        if pos == (3, 3):
            valid.append(path)
        else:
            for next_state in next_states(state):
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append(next_state)
                
    return valid
                
paths = get_paths()
part1 = min(paths, key=len)
part2 = len(max(paths, key=len))

print("Part 1: " + part1)
print("Part 2: " + str(part2))