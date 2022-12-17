import re

pattern = r"Valve ([A-Z]{2}) has flow rate=(\d{1,2}); tunnels? leads? to valves? (.+)"
lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

valves = {}

for l in lines:
    match = re.match(pattern, l)
    v = match.group(1)
    rate = int(match.group(2))
    others = [s.strip() for s in match.group(3).split(",")]

    valves[v] = {"rate": rate, "others": others}


def find_distances(rooms):
    key_rooms = {r for r in rooms if rooms[r]["rate"] > 0 or r == "AA"}
    distances = {}

    for start in rooms:
        if start not in key_rooms:
            continue

        cur, next, dist = (
            set(
                [
                    start,
                ]
            ),
            set(),
            0,
        )
        distances[(start, start)] = 0
        while cur:
            dist += 1
            for pos in cur:
                for newpos in rooms[pos]["others"]:
                    if (start, newpos) not in distances:
                        distances[(start, newpos)] = dist
                        next.add(newpos)
            cur, next = next, set()

    return distances, key_rooms


distances, key_rooms = find_distances(valves)


def find_best(cur="AA", time=30, seen=set(), targets=key_rooms):
    seen = seen | {cur}
    targets = targets - seen

    best_flow = 0
    for target in targets:
        time_left = time - distances[(cur, target)] - 1
        if time_left > 0:
            flow = valves[target]["rate"] * time_left
            flow += find_best(target, time_left, seen, targets)
            best_flow = max(flow, best_flow)
    return best_flow


part1 = find_best()
print(f"Part 1: {part1}")


# First, find all the best 26 minute flow rates
endpoints = {}


def find_and_record(cur="AA", curflow=0, time=26, seen=set()):
    seen = seen | {cur}
    targets = key_rooms - seen

    torecord = frozenset(seen - {"AA"})
    if torecord in endpoints:
        endpoints[torecord] = max(endpoints[torecord], curflow)
    else:
        endpoints[torecord] = curflow

    best_flow = 0
    for target in targets:
        time_left = time - distances[(cur, target)] - 1
        if time_left > 0:
            newflow = valves[target]["rate"] * time_left
            newflow += find_and_record(target, curflow + newflow, time_left, seen)
            if newflow > best_flow:
                best_flow = newflow
    return best_flow


find_and_record()

# Then fill in all the missing endpoints. The goal is to know the best
# flow rate to get if you 'control' a certain set of key rooms
def fill_in_endpoints(cur=frozenset(key_rooms - {"AA"})):
    if cur not in endpoints:
        best_flow = 0
        for e in cur:
            subset = cur - {e}
            new_flow = fill_in_endpoints(subset)
            if new_flow > best_flow:
                best_flow = new_flow
        endpoints[cur] = best_flow
    return endpoints[cur]


fill_in_endpoints()

# Now we iterate over all the possible assignments of key_rooms to
# human or elephant, adding together their scores.
best_flow = 0
for human_work in endpoints:
    elephant_work = frozenset(key_rooms - {"AA"} - human_work)
    total_flow = endpoints[human_work] + endpoints[elephant_work]
    if total_flow > best_flow:
        best_flow = total_flow

print(f"Part 2: {best_flow}")
