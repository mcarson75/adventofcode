code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]


def get_output(input_code, a, b):
    code = [i for i in input_code]
    pos = 0
    code[1] = a
    code[2] = b

    while code[pos] != 99:
        if code[pos] == 1:
            code[code[pos + 3]] = code[code[pos + 1]] + code[code[pos + 2]]
            pos += 4
        elif code[pos] == 2:
            code[code[pos + 3]] = code[code[pos + 1]] * code[code[pos + 2]]
            pos += 4

    return code[0]


print(f"Part 1: {get_output(code, 12, 2)}")

for noun in range(99):
    for verb in range(99):
        out = get_output(code, noun, verb)
        if out == 19690720:
            print(f"Part 2: {100*noun+verb}")
            break
