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

    def run(self):
        def printgraph():
            xmin = int(min([t.real for t in obstacles]))
            xmax = int(max([t.real for t in obstacles]))
            ymin = int(min([t.imag for t in obstacles]))
            ymax = int(max([t.imag for t in obstacles]))
            for y in range(ymin, ymax + 1):
                t = "".join(
                    [
                        (
                            "S"
                            if complex(x, y) == 0
                            else (
                                "P"
                                if complex(x, y) == pos
                                else (
                                    "O"
                                    if complex(x, y) == o2
                                    else (
                                        "#"
                                        if complex(x, y) in obstacles
                                        else "." if complex(x, y) in freespace else " "
                                    )
                                )
                            )
                        )
                        for x in range(xmin, xmax + 1)
                    ]
                )
                print(f"{t}")

        WALL = 0
        OK = 1
        TANK = 2

        obstacles = set()
        freespace = {0}
        o2 = None

        pos = 0
        dirs = {-1j: 1, 1: 4, 1j: 2, -1: 3}
        dir = -1
        history = [dir]
        backtrack = False

        while self.opcode != 99:
            output = self.parse(dirs[dir])
            if output is not None:
                if output in {WALL}:
                    obstacles.add(pos + dir)
                    dir *= 1j
                elif output in {OK, TANK}:
                    pos += dir
                    freespace.add(pos)
                    if not backtrack:
                        history.append(dir)
                    dir *= -1j
                    if output == TANK:
                        o2 = pos
                        # break
                if len(set(pos + d for d in dirs) & (freespace | obstacles)) == 4:
                    dir = -history.pop()
                    backtrack = True
                else:
                    backtrack = False

                if len(history) == 0:
                    break

        self.halted = True
        return o2, freespace
