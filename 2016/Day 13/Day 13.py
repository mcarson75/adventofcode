from collections import deque

input = 1352
finish = (31, 39)

def is_open(x, y):
    num = x*x + 3*x + 2*x*y + y + y*y + input
    return format(num, 'b').count('1') % 2 == 0 and x >= 0 and y >= 0

def next_states(state):
    moves, pos = state
    x, y = pos
    new = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    new = [i for i in new if is_open(i[0], i[1])]
    
    for (x, y) in new:
        yield moves + 1, (x, y)

queue = deque([(0, (1, 1))])
seen = {}
while queue:
    state = queue.popleft()
    moves, pos = state
    seen[pos] = moves
    
    for next_state in next_states(state):
        _moves, _pos = next_state
        if _pos not in seen or seen[_pos] > _moves:
            queue.append((_moves, _pos))

part1 = seen[finish]
part2 = len([s for s in seen.values() if s <= 50])

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
