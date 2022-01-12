# The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
# The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.

import re
from itertools import combinations, chain
from collections import deque, Counter

with open("input.txt", 'r', encoding='utf-8') as f:
    floors = [set(re.findall(r'(\w+)(?:-compatible)? (microchip|generator)', line)) for line in f.readlines()]

def is_valid_transition(floor):
    return len(set(type for _, type in floor)) < 2 or all((obj, 'generator') in floor for (obj, type) in floor if type == 'microchip')

def next_states(state):
    moves, elevator, floors = state
    
    possible_moves = chain(combinations(floors[elevator], 2), combinations(floors[elevator], 1))
    
    for move in possible_moves:
        for direction in [-1, 1]:
            next_elevator = elevator + direction
            if not next_elevator in range(len(floors)):
                continue
            
            next_floors = floors.copy()
            next_floors[elevator] = next_floors[elevator].difference(move)
            next_floors[next_elevator] = next_floors[next_elevator].union(move)
            
            if (is_valid_transition(next_floors[elevator]) and is_valid_transition(next_floors[next_elevator])):
                yield(moves + 1, next_elevator, next_floors)
                
def is_all_top_level(floors):
    return all(not floor for number, floor in enumerate(floors) if number < len(floors) - 1)

def count_floor_objects(state):
    _, elevator, floors = state
    return elevator, tuple(tuple(Counter(type for _, type in floor).most_common()) for floor in floors)

def min_moves_to_top_floor(floors):
    seen = set()
    queue = deque([(0, 0, floors)])
    
    while queue:
        state = queue.popleft()
        moves, _, floors = state
        
        if is_all_top_level(floors):
            return moves
        
        for next_state in next_states(state):
            if (key := count_floor_objects(next_state)) not in seen:
                seen.add(key)
                queue.append(next_state)
    
part1 = min_moves_to_top_floor(floors)

floors[0] = floors[0].union([('elerium', 'generator'), ('elerium', 'microchip'), ('dilithium', 'generator'), ('dilithium', 'microchip')])
part2 = min_moves_to_top_floor(floors)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))