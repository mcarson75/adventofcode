lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def initialize_monkeys():
    monkeys = {}
    for l in lines:
        m, v = l.split(": ")
        if v.isdigit():
            monkeys[m] = int(v)
        else:
            monkeys[m] = v

    return monkeys


monkeys = initialize_monkeys()


while not type(monkeys["root"]) is int:
    for m in monkeys:
        if not type(monkeys[m]) is int:
            op = monkeys[m].split(" ")
            if type(monkeys[op[0]]) is int and type(monkeys[op[2]]) is int:
                if op[1] == "+":
                    monkeys[m] = monkeys[op[0]] + monkeys[op[2]]
                elif op[1] == "-":
                    monkeys[m] = monkeys[op[0]] - monkeys[op[2]]
                elif op[1] == "*":
                    monkeys[m] = monkeys[op[0]] * monkeys[op[2]]
                elif op[1] == "/":
                    monkeys[m] = monkeys[op[0]] // monkeys[op[2]]

part1 = monkeys["root"]

print(f"Part 1: {part1}")


monkeys = initialize_monkeys()

op = monkeys["root"].split(" ")
monkeys["root"] = op[0] + " == " + op[2]
finished = {}
remove = set()

for m in monkeys:
    if type(monkeys[m]) is int:
        finished[m] = monkeys[m]
        remove.add(m)

remove.add("humn")
finished["humn"] = "X"
monkeys = {k: v for k, v in monkeys.items() if k not in remove}

while "root" not in finished:
    remove = set()
    for m in monkeys:
        op = monkeys[m].split(" ")
        if op[0] in finished and op[2] in finished:
            if op[1] == "+":
                finished[m] = f"({finished[op[0]]} + {finished[op[2]]})"
            elif op[1] == "-":
                finished[m] = f"({finished[op[0]]} - {finished[op[2]]})"
            elif op[1] == "*":
                finished[m] = f"({finished[op[0]]} * {finished[op[2]]})"
            elif op[1] == "/":
                finished[m] = f"({finished[op[0]]} // {finished[op[2]]})"
            elif op[1] == "==":
                finished[m] = f"({finished[op[0]]} == {finished[op[2]]})"
            remove.add(m)
    monkeys = {k: v for k, v in monkeys.items() if k not in remove}

a, b = finished["root"].split(" == ")
a = a[1:]
b = b[:-1]
if "X" in a:
    a, b = b, a
a = eval(a)

part2 = 0
inc = 1 << 36
while True:
    test = eval(b.replace("X", str(part2)))
    if test == a:
        break
    elif test > a:
        part2 += inc
    else:
        part2 -= inc
        inc //= 2


print(f"Part 2: {part2}")
