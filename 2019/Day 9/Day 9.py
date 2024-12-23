import intcode

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

code += [0] * 3000

part1 = intcode.computer(code).run(1)
part2 = intcode.computer(code).run(2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
