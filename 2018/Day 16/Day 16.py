import re

input = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

operations = [
    lambda R, a, b: R[a] + R[b],
    lambda R, a, b: R[a] + b,
    lambda R, a, b: R[a] * R[b],
    lambda R, a, b: R[a] * b,
    lambda R, a, b: R[a] & R[b],
    lambda R, a, b: R[a] & b,
    lambda R, a, b: R[a] | R[b],
    lambda R, a, b: R[a] | b,
    lambda R, a, b: R[a],
    lambda R, a, b: a,
    lambda R, a, b: int(a > R[b]),
    lambda R, a, b: int(R[a] > b),
    lambda R, a, b: int(R[a] > R[b]),
    lambda R, a, b: int(a == R[b]),
    lambda R, a, b: int(R[a] == b),
    lambda R, a, b: int(R[a] == R[b]),
]

part1 = 0
R = [0] * 4
n = 0
opcodes = {}
candidates = {i: set(operations) for i in range(16)}
while n < len(input):
    if "Before" in input[n]:
        bef = [int(i) for i in re.findall("\d+", input[n])]
        aft = [int(i) for i in re.findall("\d+", input[n + 2])]
        opcode, a, b, c = [int(i) for i in input[n + 1].split()]

        ops = [op(bef, a, b) == aft[c] for op in operations]
        if ops.count(True) >= 3:
            part1 += 1
        candidates[opcode] -= set(
            [operations[i] for i in range(len(operations)) if not ops[i]]
        )
        known = {k: v for k, v in candidates.items() if len(v) == 1}
        for k in known:
            opcodes[k] = list(known[k])[0]
            candidates = {c: v - known[k] for c, v in candidates.items()}
        n += 3
    elif input[n]:
        opcode, a, b, c = [int(i) for i in input[n].split()]
        R[c] = opcodes[opcode](R, a, b)
    n += 1

print(f"Part 1: {part1}")
print(f"Part 2: {R[0]}")
