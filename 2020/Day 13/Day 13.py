lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

timestamp = int(lines[0])
buses = [
    (i, int(bus_id)) for i, bus_id in enumerate(lines[1].split(",")) if bus_id != "x"
]

shortest_delay = timestamp
part1 = None
for bus in buses:
    delay = bus[1] * (timestamp // bus[1] + 1) - timestamp
    if delay < shortest_delay:
        shortest_delay = delay
        part1 = delay * bus[1]


jump = buses[0][1]
part2 = 0
for delta, bus_id in buses[1:]:
    while (part2 + delta) % bus_id != 0:
        part2 += jump
    jump *= bus_id

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
