ii, gg = [l for l in open("input.txt", "r", encoding="utf-8").read().split("\n\n")]

states = dict()
gates = list()

decimal = lambda sig: int(
    "".join(["1" if states[z] else "0" for z in sorted(sig, reverse=True)]), 2
)

for gate in gg.splitlines():
    inout = gate.split(" ")
    gates.append({"in": [inout[0], inout[2]], "out": inout[-1], "type": inout[1]})
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
        i1, i2 = gate["in"]
        if states[i1] is not None and states[i2] is not None:
            out = gate["out"]
            if gate["type"] == "OR":
                states[out] = states[i1] | states[i2]
            elif gate["type"] == "AND":
                states[out] = states[i1] & states[i2]
            if gate["type"] == "XOR":
                states[out] = states[i1] ^ states[i2]

part1 = decimal(zsigs)

des_bin = bin(desired_output)
act_bin = bin(part1)
indices = []
for n in range(len(des_bin) - 2):
    if des_bin[n] != act_bin[n]:
        indices.append(f"z{len(des_bin) - n - 1:02}")

print(f"Part 1: {part1}")

gatedict = {g["out"]: {"in": g["in"], "type": g["type"]} for g in gates}


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


def get_ins(sig):
    return {k: v for k, v in gatedict.items() if sig in v["in"]}
    # return [g for g in gates if sig in g["in"]]


# def get_outs(sig):

# return [g for g in gates if sig in g["out"]]


def get_all_ins(sig1, sig2):
    return {k: v for k, v in gatedict.items() if sig1 in v["in"] and sig2 in v["in"]}
    # return [g for g in gates if sig1 in g["in"] and sig2 in g["in"]]


# def find_parents(sig):
#     parents = set()
#     parent_gates = []
#     for g in (gate for gate in gates if gate["out"] == sig):
#         parent_gates.append(g)
#         parents |= set(g["in"])
#         for i in g["in"]:
#             if not i.startswith("x") and not i.startswith("y"):
#                 p, pg = find_parents(i)
#                 parents |= p
#                 parent_gates += g
#     return parents, parent_gates


# error_states = {s for s in states}
# error_gates = [g for g in gates]
# for z in indices:
#     p, g = find_parents(z)
#     error_states &= p
#     error_gates = [g for eg in error_gates if eg in g]


def gate_swap(sig1, sig2):
    g1 = gatedict[sig1]
    g2 = gatedict[sig2]
    gatedict[sig1] = g2
    gatedict[sig2] = g1


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
