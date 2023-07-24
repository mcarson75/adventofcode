instrs = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

pos = 0
dir = 1
dirs = [1, -1j, -1, 1j]

for inst in instrs:
    move, amount = inst[0], int(inst[1:])
    if move == "N":
        pos += amount * 1j
    elif move == "S":
        pos += amount * -1j
    elif move == "E":
        pos += amount
    elif move == "W":
        pos -= amount
    elif move == "L":
        shift = amount // 90
        ind = dirs.index(dir)
        dir = dirs[(ind - shift) % 4]
    elif move == "R":
        shift = amount // 90
        ind = dirs.index(dir)
        dir = dirs[(ind + shift) % 4]
    elif move == "F":
        pos += dir * amount


print(f"Part 1: {int(abs(pos.real)+abs(pos.imag))}")

dir_right = [1, -1j, -1, 1j]
dir_left = [1, 1j, -1, -1j]

pos = 0
waypoint = 10 + 1j
for inst in instrs:
    move, amount = inst[0], int(inst[1:])
    if move == "N":
        waypoint += amount * 1j
    elif move == "S":
        waypoint += amount * -1j
    elif move == "E":
        waypoint += amount
    elif move == "W":
        waypoint -= amount
    elif move == "L":
        shift = amount // 90
        waypoint *= dir_left[shift]
    elif move == "R":
        shift = amount // 90
        waypoint *= dir_right[shift]
    elif move == "F":
        pos += waypoint * amount

print(f"Part 2: {int(abs(pos.real)+abs(pos.imag))}")
