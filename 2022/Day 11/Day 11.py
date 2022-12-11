from math import prod, lcm
from copy import deepcopy

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

monkeys = []

for n in range(0, len(lines), 7):
    group = lines[n : n + 7]
    m = {"inspect": 0}
    m["items"] = [int(i) for i in group[1].split(":")[1].split(",")]
    m["operator"], m["operand"] = group[2].split()[4:]
    m["test"] = int(group[3].split()[3])
    m["true"] = int(group[4].split()[5])
    m["false"] = int(group[5].split()[5])
    monkeys.append(m)


def monkey_business(ms, rounds, reduce_worry):
    LCM = lcm(*([m["test"] for m in ms]))

    for n in range(rounds):
        for m in ms:
            for worry in m["items"]:
                op = worry if m["operand"] == "old" else int(m["operand"])
                worry = worry * op if m["operator"] == "*" else worry + op
                if reduce_worry:
                    worry //= 3
                worry = worry % LCM
                ms[m["false"] if worry % m["test"] else m["true"]]["items"].append(
                    worry
                )
            m["inspect"] += len(m["items"])
            m["items"] = []

    inspect = [m["inspect"] for m in ms]
    inspect.sort()

    return prod(inspect[-2:])


print(f"Part 1: {monkey_business(deepcopy(monkeys), 20, True)}")
print(f"Part 2: {monkey_business(deepcopy(monkeys), 10000, False)}")
