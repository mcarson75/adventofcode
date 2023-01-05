from collections import deque

commands = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def run_program(a):
    regs = "abcdefgh"
    reg = {k: 0 for k in regs}
    reg["a"] = a
    get_val = lambda v: reg[v] if v.isalpha() else int(v)

    pos = 0
    muls = 0
    while pos in range(len(commands)):

        command, r, op = commands[pos][:3], commands[pos][4], commands[pos][6:]
        if command == "set":
            reg[r] = get_val(op)
        elif command == "mul":
            reg[r] *= get_val(op)
            muls += 1
        elif command == "sub":
            reg[r] -= get_val(op)
        elif command == "jnz" and get_val(r) != 0:
            pos += get_val(op) - 1
        pos += 1

    return muls


print(f"Part 1: {run_program(0)}")

part2 = 0
for x in range(108400, 108400 + 17000 + 1, 17):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            part2 += 1
            break

print(f"Part 2: {part2}")
