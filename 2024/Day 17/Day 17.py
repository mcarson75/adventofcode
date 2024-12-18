input = [
    l.rstrip().split(": ") for l in open("input.txt", "r", encoding="utf-8").readlines()
]


registers = {}
for line in input[:3]:
    registers[line[0][-1]] = int(line[1])

commands = [int(i) for i in input[-1][1].split(",")]
pos = 0


def combo(operand, reg):
    if operand == 4:
        return reg["A"]
    elif operand == 5:
        return reg["B"]
    if operand == 6:
        return reg["C"]
    return operand


def do_op(commands, reg, a=None):
    pos = 0
    output = []
    if not a is None:
        reg["A"] = a
    while pos < len(commands):
        opcode, operand = commands[pos : pos + 2]
        if opcode == 0:
            reg["A"] //= 2 ** combo(operand, reg)
        elif opcode == 1:
            reg["B"] ^= operand
        elif opcode == 2:
            reg["B"] = combo(operand, reg) % 8
        elif opcode == 3:
            if not reg["A"] == 0:
                pos = operand
            else:
                pos += 2
        elif opcode == 4:
            reg["B"] ^= reg["C"]
        elif opcode == 5:
            output.append(combo(operand, reg) % 8)
        elif opcode == 6:
            reg["B"] = reg["A"] // (2 ** combo(operand, reg))
        elif opcode == 7:
            reg["C"] = reg["A"] // (2 ** combo(operand, reg))
        if opcode != 3:
            pos += 2
    return output


output = do_op(commands, registers.copy())
part1 = ",".join([str(i) for i in output])

poss = [0]
for i in range(len(commands)):
    match = commands[-(i + 1) :]
    new_poss = []
    while poss:
        p = poss.pop(0) * 8
        for n in range(p, p + 8):
            if do_op(commands, registers.copy(), n) == match:
                new_poss.append(n)
    poss = new_poss

part2 = min(poss)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
