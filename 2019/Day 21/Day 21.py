import intcode

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

code += [0] * 3000

vm = intcode.computer(code)

springscript = [
    "NOT A T",
    "NOT B J",
    "OR T J",
    "NOT C T",
    "OR T J",
    "AND D J",
    "WALK",
]

ascii_chars = list(map(ord, list("\n".join(springscript) + "\n")))

vm.run(ascii_chars)

if vm.output[-1] <= 255:
    print("".join([chr(_) for _ in vm.output]))
else:
    print(f"Part 1: {vm.output[-1]}")


vm = intcode.computer(code)

springscript = [
    "NOT A T",
    "NOT B J",
    "OR T J",
    "NOT C T",
    "OR T J",
    "AND D J",
    "NOT E T",
    "NOT T T",
    "OR H T",
    "AND T J",
    "RUN",
]

ascii_chars = list(map(ord, list("\n".join(springscript) + "\n")))

vm.run(ascii_chars)

if vm.output[-1] <= 255:
    print("".join([chr(_) for _ in vm.output]))
else:
    print(f"Part 2: {vm.output[-1]}")
