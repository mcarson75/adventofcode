import intcode

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

code += [0] * 3000

map, robot_pos, robot_dir = intcode.computer(code).get_map()

intersections = set(m for m in map if all(m + d in map for d in [-1, 1, 1j, -1j]))
part1 = sum(int(i.real * i.imag) for i in intersections)

print(f"Part 1: {part1}")

code[0] = 2
part2 = intcode.computer(code).move_robot(map, robot_pos, robot_dir)

print(f"Part 2: {part2}")
