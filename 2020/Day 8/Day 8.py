from copy import deepcopy

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

instr = {}
for n in range(len(lines)):
    op, arg = lines[n].split(" ")
    instr[n] = {"op": op, "arg": int(arg), "exec": False}


def run_code(instr):
    pointer = 0
    acc = 0
    finished = False
    while True:
        if pointer > len(instr) - 1:
            finished = True
            break
        if instr[pointer]["exec"] == True:
            break
        instr[pointer]["exec"] = True
        if instr[pointer]["op"] == "nop":
            pointer += 1
        elif instr[pointer]["op"] == "jmp":
            pointer += instr[pointer]["arg"]
        elif instr[pointer]["op"] == "acc":
            acc += instr[pointer]["arg"]
            pointer += 1

    return acc, finished


part1, finished = run_code(deepcopy(instr))

print(f"Part 1: {part1}")

pointer = 0
finished = False
while not finished:
    new_instr = deepcopy(instr)
    if new_instr[pointer]["op"] == "acc":
        pointer += 1
        continue
    elif new_instr[pointer]["op"] == "nop":
        new_instr[pointer]["op"] = "jmp"
    elif new_instr[pointer]["op"] == "jmp":
        new_instr[pointer]["op"] = "nop"
    acc, finished = run_code(new_instr)
    pointer += 1

print(f"Part 2: {acc}")
