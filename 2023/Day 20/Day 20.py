from math import lcm

PRESSES = 1000
TARGET_MODULE = "rx"

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


class Module:
    def __init__(self, line):
        self.pulses = [0, 0]
        self.state = False
        if "->" not in line:
            self.name = line
            self.type = "output"
            return
        self.name, dst = line.split(" -> ")
        self.dest = dst.split(", ")
        self.inputs = {}
        if self.name[0] == "%":
            self.type = "flipflop"
            self.name = self.name[1:]
        elif self.name[0] == "&":
            self.type = "conjunction"
            self.name = self.name[1:]
        else:
            self.type = "broadcast"

    def __repr__(self):
        return self.name

    def go(self, src, input):
        if self.type == "output":
            self.state = input
            return []
        elif self.type == "flipflop":
            if not input:
                self.state = not self.state
            else:
                return []
        elif self.type == "conjunction":
            self.inputs[src] = input
            self.state = not all(self.inputs.values())

        self.pulses[self.state] += len(self.dest)
        return [(d, self.name, self.state) for d in self.dest]


mods = set(Module(line) for line in lines)
modules = {m.name: m for m in mods}

outputs = []
for module in modules:
    for d in modules[module].dest:
        if d in modules:
            modules[d].inputs[module] = False
        else:
            if d == TARGET_MODULE:
                target_src = module
            outputs.append(Module(d))

modules |= {m.name: m for m in outputs}

triggers = {k: 0 for k in modules[target_src].inputs}
button = 0
while True:
    queue = [("broadcaster", None, None)]
    if button == PRESSES:
        lo = sum([m.pulses[0] for m in modules.values()]) + PRESSES
        hi = sum([m.pulses[1] for m in modules.values()])
    button += 1
    if all(t > 0 for t in triggers.values()):
        break
    while queue:
        module, src, input = queue[0]
        queue = queue[1:]
        queue += modules[module].go(src, input)
        on_state = [m for m in modules[target_src].inputs if modules[m].state]
        triggers.update({o: button for o in on_state})

print(f"Part 1: {lo*hi}")
print(f"Part 2: {lcm(*triggers.values())}")
