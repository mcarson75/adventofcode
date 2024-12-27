ii, gg = [l for l in open("input.txt", "r", encoding="utf-8").read().split("\n\n")]

states = dict()
gates = dict()

decimal = lambda sig: int(
    "".join(["1" if states[z] else "0" for z in sorted(sig, reverse=True)]), 2
)

for gate in gg.splitlines():
    inout = gate.split(" ")
    gates[inout[-1]] = {"in": [inout[0], inout[2]], "type": inout[1]}
    for sig in inout[::2]:
        states[sig] = None

for input in ii.splitlines():
    sig, value = input.split(": ")
    states[sig] = True if value == "1" else False

xsigs = set(s for s in states if s.startswith("x"))
ysigs = set(s for s in states if s.startswith("y"))
zsigs = set(s for s in states if s.startswith("z"))

inputs = [decimal(xsigs), decimal(ysigs)]
desired_output = sum(inputs)

while any([states[z] == None for z in zsigs]):
    for gate in gates:
        i1, i2 = gates[gate]["in"]
        type = gates[gate]["type"]
        if states[i1] is not None and states[i2] is not None:
            out = gate
            if type == "OR":
                states[out] = states[i1] | states[i2]
            elif type == "AND":
                states[out] = states[i1] & states[i2]
            if type == "XOR":
                states[out] = states[i1] ^ states[i2]

part1 = decimal(zsigs)

print(f"Part 1: {part1}")

get_ins = lambda sig: {k: v for k, v in gates.items() if sig in v["in"]}
get_all_ins = lambda sig1, sig2: {
    k: v for k, v in gates.items() if sig1 in v["in"] and sig2 in v["in"]
}


def gate_swap(sig1, sig2):
    g1 = gates[sig1]
    g2 = gates[sig2]
    gates[sig1] = g2
    gates[sig2] = g1


# Assumption is that all errors are within a particular bit and not between bits
def fix_adder(n, cin=None):
    swaps = {}
    in1 = f"x{n:02}"
    in2 = f"y{n:02}"
    out = f"z{n:02}"
    g = get_all_ins(in1, in2)
    if not cin:
        gx = gates[out]
        if gx["type"] != "XOR":
            swaps = set(g.keys())
            gate_swap(*swaps)
            g = get_all_ins(in1, in2)
        carry = [k for k, v in g.items() if v["type"] == "AND"][0]

    return swaps, carry


fix_adder(0)

des_bin = bin(desired_output)
act_bin = bin(part1)
indices = []
for n in range(len(des_bin) - 2):
    if des_bin[n] != act_bin[n]:
        indices.append(f"z{len(des_bin) - n - 1:02}")


invalid_gates = dict()
for z in range(len(zsigs)):
    sig = f"z{z:02}"
    if z < len(zsigs) - 1 and gatedict[sig]["type"] != "XOR":
        invalid_gates[sig] = gatedict[sig]
    elif z == len(zsigs) - 1 and gatedict[sig]["type"] != "OR":
        invalid_gates[sig] = gatedict[sig]

# invalid gates
# sgj, z35
# kpp, z31
# vss, z14
# hjf, kdh


invalid = [("sgj", "z35"), ("kpp", "z31"), ("vss", "z14"), ("kdh", "hjf")]
for i in invalid:
    gate_swap(*i)

states = dict()
for g in gatedict:
    states[g] = None
    for i in gatedict[g]["in"]:
        states[i] = None

for input in ii.splitlines():
    sig, value = input.split(": ")
    states[sig] = True if value == "1" else False

while any([states[z] == None for z in zsigs]):
    for gate in gatedict:
        i1, i2 = gatedict[gate]["in"]
        if states[i1] is not None and states[i2] is not None:
            if gatedict[gate]["type"] == "OR":
                states[gate] = states[i1] | states[i2]
            elif gatedict[gate]["type"] == "AND":
                states[gate] = states[i1] & states[i2]
            if gatedict[gate]["type"] == "XOR":
                states[gate] = states[i1] ^ states[i2]

check = decimal(zsigs)

des_bin = bin(desired_output)
act_bin = bin(check)
indices = []
for n in range(len(des_bin) - 2):
    if des_bin[n] != act_bin[n]:
        indices.append(f"z{len(des_bin) - n - 1:02}")

part2 = ",".join(sorted([i for pair in invalid for i in pair]))
print(f"Part 2: {part2}")
