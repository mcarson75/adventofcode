class computer:
    def __init__(self, code, phase=None):
        self.pos = 0
        self.phase = phase
        self.code = [i for i in code]
        self.output = []
        self.opcode = 1
        self.phase_used = False if phase else True
        self.halted = False
        self.relative_base = 0

    def __repr__(self):
        return str(self.phase)

    def parse(self, input, debug=False):
        def get_index(strcode, which):
            mode = int(strcode[3 - which])
            index = self.pos + which

            if mode == 0:
                return self.code[index]
            if mode == 1:
                return index
            if mode == 2:
                return self.code[index] + self.relative_base

        def get_parm(strcode, which):
            return self.code[get_index(strcode, which)]

        strcode = "{:0>5}".format(self.code[self.pos])
        self.opcode = int(strcode[-2:])
        if debug:
            print(f"pos: {self.pos} - current opcode: {self.opcode} - {strcode}")
        if self.opcode == 99:
            return

        if self.opcode == 1:
            a = get_parm(strcode, 1)
            b = get_parm(strcode, 2)
            c = get_index(strcode, 3)

            if debug:
                print(f"Opcode {self.opcode}: Altered {self.code[c]} at {c} to {a+b}")
            self.code[c] = a + b
            self.pos += 4
        elif self.opcode == 2:
            a = get_parm(strcode, 1)
            b = get_parm(strcode, 2)
            c = get_index(strcode, 3)

            if debug:
                print(f"Opcode {self.opcode}: Altered {self.code[c]} at {c} to {a*b}")
            self.code[c] = a * b
            self.pos += 4
        elif self.opcode == 3:
            a = get_index(strcode, 1)
            if debug:
                print(f"Opcode {self.opcode}: Altered {self.code[a]} at {a} to {input}")
            self.code[a] = input
            self.pos += 2
        elif self.opcode == 4:
            a = get_parm(strcode, 1)
            if debug:
                print(f"Opcode {self.opcode}: {a} added to output")
            self.output.append(a)
            self.pos += 2
            return a

        elif self.opcode == 5:
            a = get_parm(strcode, 1)
            b = get_parm(strcode, 2)
            if a != 0:
                if debug:
                    print(f"Opcode {self.opcode}: {a} != 0. pos from {self.pos} to {b}")
                self.pos = b
            else:
                if debug:
                    print(f"Opcode {self.opcode}: {a} == 0. noop")
                self.pos += 3
        elif self.opcode == 6:
            a = get_parm(strcode, 1)
            b = get_parm(strcode, 2)
            if a == 0:
                if debug:
                    print(f"Opcode {self.opcode}: {a} == 0. pos from {self.pos} to {b}")
                self.pos = b
            else:
                if debug:
                    print(f"Opcode {self.opcode}: {a} != 0. noop")
                self.pos += 3
        elif self.opcode == 7:
            a = get_parm(strcode, 1)
            b = get_parm(strcode, 2)
            c = get_index(strcode, 3)

            if debug:
                print(
                    f"Opcode {self.opcode}: Altered {self.code[c]} at {c} to {int(a<b)}"
                )
            self.code[c] = int(a < b)
            self.pos += 4
        elif self.opcode == 8:
            a = get_parm(strcode, 1)
            b = get_parm(strcode, 2)
            c = get_index(strcode, 3)

            if debug:
                print(
                    f"Opcode {self.opcode}: Altered {self.code[c]} at {c} to {int(a==b)}"
                )
            self.code[c] = int(a == b)
            self.pos += 4
        elif self.opcode == 9:
            a = get_parm(strcode, 1)
            self.relative_base += a
            if debug:
                print(f"Opcode {self.opcode}: Relative base now {self.relative_base}")
            self.pos += 2
        return None

    def run(self, input):
        pos = 0
        dir = -1j
        tiles = {0: input}
        instructions = []

        while self.opcode != 99:
            if pos not in tiles:
                tiles[pos] = 0
            output = self.parse(tiles[pos])
            if output is not None:
                if len(instructions) <= 1:
                    instructions.append(output)
                if len(instructions) == 2:
                    color, turn = instructions
                    instructions = []
                    tiles[pos] = color
                    if turn:
                        dir *= 1j
                    else:
                        dir *= -1j
                    pos += dir

        self.halted = True
        return tiles
