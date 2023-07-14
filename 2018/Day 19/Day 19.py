lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

instructions = []
ip = 0

for line in lines:
    if "#ip" in line:
        ip_index = int(line.split()[1])
    else:
        opcode, a, b, c = line.split()
        instructions.append({"opcode": opcode, "a": int(a), "b": int(b), "c": int(c)})

operations = {
    "addr": lambda R, a, b: R[a] + R[b],
    "addi": lambda R, a, b: R[a] + b,
    "mulr": lambda R, a, b: R[a] * R[b],
    "muli": lambda R, a, b: R[a] * b,
    "banr": lambda R, a, b: R[a] & R[b],
    "bani": lambda R, a, b: R[a] & b,
    "borr": lambda R, a, b: R[a] | R[b],
    "bori": lambda R, a, b: R[a] | b,
    "setr": lambda R, a, b: R[a],
    "seti": lambda R, a, b: a,
    "gtir": lambda R, a, b: int(a > R[b]),
    "gtri": lambda R, a, b: int(R[a] > b),
    "gtrr": lambda R, a, b: int(R[a] > R[b]),
    "eqir": lambda R, a, b: int(a == R[b]),
    "eqri": lambda R, a, b: int(R[a] == b),
    "eqrr": lambda R, a, b: int(R[a] == R[b]),
}


def do_op(inst, reg):
    reg[inst["c"]] = operations[inst["opcode"]](reg, inst["a"], inst["b"])

    return reg


def run(reg):
    t = 0
    while reg[ip_index] in range(len(instructions)):
        reg = do_op(instructions[reg[ip_index]], reg)
        reg[ip_index] += 1

        t += 1
        if t > 10000000:
            print(reg)

    return reg[0]


# print(f"Part 1: {run([0]*6)}")

print(f"Part 2: {run([1, 0, 0, 0, 0, 0])}")
