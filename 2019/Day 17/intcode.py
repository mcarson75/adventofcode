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

    def get_map(self):
        def printgraph():
            xmin = int(min([t.real for t in map]))
            xmax = int(max([t.real for t in map]))
            ymin = int(min([t.imag for t in map]))
            ymax = int(max([t.imag for t in map]))
            for y in range(ymin, ymax + 1):
                t = "".join(
                    [
                        "#" if complex(x, y) in map else "."
                        for x in range(xmin, xmax + 1)
                    ]
                )
                print(f"{t}")

        map = set()
        pos = 0
        dirs = {"v": 1j, "^": -1j, "<": -1, ">": 1}

        while self.opcode != 99:
            output = self.parse(0)
            if output is not None:
                if output == 10:
                    pos = (pos.imag + 1) * 1j
                elif chr(output) == ".":
                    pos += 1
                elif chr(output) == "#":
                    map.add(pos)
                    pos += 1
                elif chr(output) in {"v", "^", "<", ">"}:
                    map.add(pos)
                    robot_pos = pos
                    robot_dir = dirs[chr(output)]
                    pos += 1

        self.halted = True
        return map, robot_pos, robot_dir

    def move_robot(self, map, robot_pos, robot_dir):
        path = []
        current_length = 0
        while True:
            if robot_pos + robot_dir in map:
                current_length += 1
                robot_pos += robot_dir
            else:
                if current_length > 0:
                    path.append(str(current_length))
                if robot_pos + (robot_dir * -1j) in map:
                    path.append("L")
                    current_length = 0
                    robot_dir *= -1j
                elif robot_pos + (robot_dir * 1j) in map:
                    path.append("R")
                    current_length = 0
                    robot_dir *= 1j
                else:
                    # path = path[:-3]
                    break

        pathstring = ",".join(path)
        moves = [path[i] + path[i + 1] for i in range(0, len(path), 2)]
        seq = " ".join(moves)
        functions = dict()

        for a_e in range(2, 8):
            for b_s in range(a_e + 1, len(moves) - 3):
                for b_e in range(b_s + 2, b_s + 10):
                    a = " ".join(moves[:a_e])
                    b = " ".join(moves[b_s:b_e])
                    rem = seq.replace(a, "|").replace(b, "|")
                    _, min_c = min(
                        (len(c.strip()), c.strip())
                        for c in rem.split("|")
                        if len(c.strip()) > 0
                    )
                    rem = rem.replace(min_c, "").replace(" ", "").replace("|", "")
                    if len(rem) == 0:
                        functions["A"] = a
                        functions["B"] = b
                        functions["C"] = min_c

        for group in ["A", "B", "C"]:
            temp = ""
            for move in functions[group].split(" "):
                temp += f"{move[0]},{move[1:]},"
            functions[group] = temp[:-1]
            pathstring = pathstring.replace(functions[group], group)

        inputstring = (
            f"{pathstring}\n{functions['A']}\n{functions['B']}\n{functions['C']}\nn\n"
        )

        all_input = [ord(i) for i in inputstring]
        input = all_input.pop(0)
        self.__init__(self.code)

        last_output = None
        while self.opcode != 99:
            output = self.parse(input)
            if output is not None:
                last_output = output
            if self.opcode == 3 and len(all_input) > 0:
                input = all_input.pop(0)

        self.halted = True
        return last_output
