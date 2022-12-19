import re

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

costs = list()
for l in lines:
    costs.append([int(i) for i in re.findall("\d+", l)])


def most_geodes(cost, queue_size=5000, total_time=24):
    time = 0
    depth = 0
    most = 0
    seen = set()
    q = [((1, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), 0)]
    while q:
        robot, resource, mined, time = q.pop(0)
        if (robot, resource, mined, time) in seen:
            continue
        seen.add((robot, resource, mined, time))
        if time > depth:
            q.sort(
                key=lambda m: m[2][3] * 1000 + m[2][2] * 100 + m[2][1] * 10 + m[2][0],
                reverse=True,
            )
            q = q[:queue_size]
            depth = time
        if time == total_time:
            most = max(most, mined[3])
            continue
        new_resource = tuple([resource[i] + robot[i] for i in range(4)])
        new_mined = tuple([mined[i] + robot[i] for i in range(4)])
        q.append((robot, new_resource, new_mined, time + 1))
        for i in range(4):
            c = cost[i]
            if all([resource[j] >= c[j] for j in range(4)]):
                new_robot = list(robot)
                new_robot[i] += 1
                new_robot = tuple(new_robot)

                adj_new_resource = tuple([new_resource[j] - c[j] for j in range(4)])
                q.append((new_robot, adj_new_resource, new_mined, time + 1))

    return most


part1 = 0
part2 = 1
for id, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs in costs:
    cost = [
        (ore_ore, 0, 0, 0),
        (clay_ore, 0, 0, 0),
        (obs_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_obs, 0),
    ]
    g = most_geodes(cost)
    part1 += id * g
    print(f"Blueprint {id}: {g} geodes")
    if id <= 3:
        part2 *= most_geodes(cost, queue_size=10000, total_time=32)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
