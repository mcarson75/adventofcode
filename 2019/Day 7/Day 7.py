import intcode
from itertools import permutations


class amplifier:
    def __init__(self, phase):
        self.pos = 0
        self.phase = phase
        self.code = [i for i in code]
        self.output = 0
        self.opcode = 1
        self.phase_used = False
        self.halted = False

    def __repr__(self):
        return str(self.phase)

    def run(self, input):
        while self.opcode != 99:
            if not self.phase_used:
                self.opcode, new_pos, out = intcode.parse_code(
                    self.code, self.pos, self.phase
                )
                self.phase_used = True
            else:
                self.opcode, new_pos, out = intcode.parse_code(
                    self.code, self.pos, input
                )
            self.pos = new_pos
            if out:
                self.output = out
                return self.output

        self.halted = True
        return self.output


code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

out_signal = 0

for perm in permutations([0, 1, 2, 3, 4]):
    amps = [amplifier(p) for p in perm]
    out = 0
    for amp in amps:
        out = amp.run(out)
    out_signal = max(out, out_signal)


print(f"Part 1: {out_signal}")

for perm in permutations([5, 6, 7, 8, 9]):
    amps = [amplifier(p) for p in perm]
    out = 0
    while not all(a.halted for a in amps):
        for amp in amps:
            out = amp.run(out)
    out_signal = max(out, out_signal)

print(f"Part 2: {out_signal}")
