def parse_code(code, pos, input):
    strcode = "{:0>5}".format(code[pos])
    opcode = int(strcode[-2:])
    if opcode == 99:
        return 99, None, None
    par_a = (
        code[pos + 1] if opcode in [3, 4] or int(strcode[2]) else code[code[pos + 1]]
    )

    if opcode in [1, 2, 5, 6, 7, 8]:
        par_b = code[pos + 2] if int(strcode[1]) else code[code[pos + 2]]

    output = None

    if opcode in [1, 2, 7, 8]:
        out = code[pos + 3]
        new_pos = pos + 4
    elif opcode in [3, 4]:
        out = code[pos + 1]
        new_pos = pos + 2
    else:
        out = None
        new_pos = pos + 3

    if opcode == 1:
        code[out] = par_a + par_b
    elif opcode == 2:
        code[out] = par_a * par_b
    elif opcode == 3:
        code[par_a] = input
    elif opcode == 4:
        output = code[par_a]
    elif opcode == 5:
        if par_a != 0:
            new_pos = par_b
    elif opcode == 6:
        if par_a == 0:
            new_pos = par_b
    elif opcode == 7:
        if par_a < par_b:
            code[out] = 1
        else:
            code[out] = 0
    elif opcode == 8:
        if par_a == par_b:
            code[out] = 1
        else:
            code[out] = 0

    return opcode, new_pos, output


def run(input_code, input, phase=None):
    code = [i for i in input_code]
    pos = 0
    output = 0

    opcode = 1

    input_index = 0
    if phase is not None:
        input = [phase] + [input]
    else:
        input = [input]

    while opcode != 99:
        opcode, new_pos, out = parse_code(code, pos, input[input_index])
        if opcode == 3:
            input_index = 1
        if out:
            output = out
        pos = new_pos

    return output
