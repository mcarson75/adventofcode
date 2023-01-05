from collections import deque

commands = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def run_program(pid, i, o):
    reg = {"p": pid}
    get_val = lambda v: reg[v] if v.isalpha() else int(v)

    pos = 0
    while pos in range(len(commands)):

        command, r, op = commands[pos][:3], commands[pos][4], commands[pos][6:]
        if command == "set":
            reg[r] = get_val(op)
        elif command == "add":
            reg[r] += get_val(op)
        elif command == "mul":
            reg[r] *= get_val(op)
        elif command == "mod":
            reg[r] %= get_val(op)
        elif command == "jgz" and get_val(r) > 0:
            pos += get_val(op) - 1
        elif command == "snd":
            o.append(get_val(r))
            yield "send"
        elif command == "rcv":
            while not i:
                yield "wait"
            else:
                reg[r] = i.popleft()
                yield "recd"
        pos += 1


queue = deque()
for s in run_program(0, queue, queue):
    if s == "recd":
        part1 = queue[-1]
        break

print(f"Part 1: {part1}")

queue0, queue1 = deque(), deque()
program0, program1 = run_program(0, queue1, queue0), run_program(1, queue0, queue1)
part2 = 0
while True:
    a, b = next(program1), next(program0)
    part2 += a == "send"
    if {a, b} == {"wait"}:
        break

print(f"Part 2: {part2}")
