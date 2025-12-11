from scipy import optimize

lines = [
    l.strip("\n").split(" ")
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]

transpose = lambda array: [list(a) for a in zip(*array)]

part1 = part2 = 0
for line in lines:
    lights = int(line[0][1:-1].replace(".", "0").replace("#", "1"), 2)
    buttons_dec = []
    buttons = []
    for button in line[1:-1]:
        ind = [int(i) for i in button[1:-1].split(",")]
        bs = [1 if i in ind else 0 for i in range(len(line[0][1:-1]))]
        buttons.append(bs)
        buttons_dec.append(int("".join([str(i) for i in bs]), 2))
    joltage = [int(i) for i in line[-1][1:-1].split(",")]

    init = 0
    visited = {init}
    q = [(init, 0)]
    while q:
        prev, n = q.pop(0)
        if prev == lights:
            part1 += n
            break
        for b in buttons_dec:
            xor = prev ^ b
            if xor not in visited:
                visited.add(xor)
                q.append((xor, n + 1))

    c = [1] * len(buttons)
    part2 += int(
        sum(optimize.linprog(c, A_eq=transpose(buttons), b_eq=joltage, integrality=1).x)
    )


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
