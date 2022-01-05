from functools import lru_cache

#rooms = (("D", "B"), ("A", "A"), ("B", "D"), ("C", "C"))

rooms = (("D", "D", "D", "B"), ("A", "C", "B", "A"), ("B", "B", "A", "D"), ("C", "A", "C", "C"))

room_map = (2, 4, 6, 8)
hall_spots = (0, 1, 3, 5, 7, 9, 10)
destination = {"A": 0, "B": 1, "C": 2, "D": 3}
costs = {"A": 1, "B": 10, "C": 100, "D": 1000}

room_size = len(rooms[0])

hallway_start = tuple(None for _ in range(len(room_map) + len(hall_spots)))

@lru_cache(maxsize=None)
def solve(hall, rooms):
    if rooms == (("A",) * room_size, ("B",) * room_size, ("C",) * room_size, ("D",) * room_size):
        return 0

    best_cost = float('inf')
    for i, pod in enumerate(hall):  # Move from the hallway into a room.
        if pod is None:
            continue
        dest = destination[pod]

        if any([r is not None and r != pod for r in rooms[dest]]):  # Check if room is available
            continue

        offset = 1 if room_map[dest] > i else -1
        if any(hall[i + offset:room_map[dest] + offset:offset]): # Check if path to room is empty
            continue

        empty_count = sum(elem is None for elem in rooms[dest])
        new_room = (None,) * (empty_count - 1) + (pod,) * (room_size - empty_count + 1)
        steps = empty_count + abs(i - room_map[dest])
        cost = steps * costs[pod]
        next_result = solve(hall[:i] + (None,) + hall[i + 1:], rooms[:dest] + (new_room,)
                                + rooms[dest + 1:])
        best_cost = min(cost + next_result, best_cost)
    for i, room in enumerate(rooms):  # Move from a room into the hallway.
        if not any([p is not None and destination[p] != i for p in room]): # Check if any pods in room should move
            continue
        empty_count = sum(elem is None for elem in room)
        steps = empty_count + 1
        pod = room[empty_count]
        hall_check = tuple(h for h in hall_spots if not any(hall[min(h, room_map[i]): max(h, room_map[i]) + 1]))
        for hall_destination in hall_check:
            destination_steps = steps + abs(hall_destination - room_map[i])
            cost = destination_steps * costs[pod]
            new_room = (None,) * (empty_count + 1) + room[empty_count + 1:]
            next_result = solve(
                hall[:hall_destination] + (pod,) + hall[hall_destination + 1:],
                rooms[:i] + (new_room,) + rooms[i + 1:])
            new_cost = cost + next_result
            if new_cost < best_cost:
                best_cost = new_cost

    return best_cost

cost = solve(hallway_start, rooms)

print(cost)