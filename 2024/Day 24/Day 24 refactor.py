ii, gg = [l for l in open("input.txt", "r", encoding="utf-8").read().split("\n\n")]

states = dict()
gates = dict()

decimal = lambda sig: int(
    "".join(["1" if states[z] else "0" for z in sorted(sig, reverse=True)]), 2
)

for gate in gg.splitlines():
    inout = gate.split(" ")
    gates[inout[-1]] = {"in": {inout[0], inout[2]}, "type": inout[1]}
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


def get_all_gates(n, cin):
    gates = set()
    in1 = f"x{n:02}"
    in2 = f"y{n:02}"
    out = f"z{n:02}"
    gates.add(out)
    gates |= set(get_ins(cin).keys())
    gates |= set(get_all_ins(in1, in2).keys())
    new_gates = set()
    for g in gates:
        new_gates |= set(get_ins(g))
    gates |= new_gates

    return gates


def gate_swap(sig1, sig2):
    g1 = gates[sig1]
    g2 = gates[sig2]
    gates[sig1] = g2
    gates[sig2] = g1


# Assumption is that all errors are within a particular bit and not between bits
def fix_adder(n, cin=None):
    swaps = set()
    in1 = f"x{n:02}"
    in2 = f"y{n:02}"
    out = f"z{n:02}"
    g = get_all_ins(in1, in2)
    gz = gates[out]
    if not cin:
        if gz["type"] != "XOR":
            swaps = set(g.keys())
            gate_swap(*swaps)
            g = get_all_ins(in1, in2)
        carry = [k for k, v in g.items() if v["type"] == "AND"][0]
    else:
        g_adder = get_all_gates(n, cin)
        if len(g_adder) != 5:
            print("stop")
        g_ins = set(get_all_ins(in1, in2))

        # Assumes inputs are correct, so there will be an XOR and AND
        for g in g_ins:
            g_next = set(gates[v]["type"] for v in set(get_ins(g)))
            checked.add(g)
            if gates[g]["type"] == "XOR":
                output_in = g
                if g_next == {"XOR", "AND"}:
                    g_adder.remove(g)
            elif gates[g]["type"] == "AND":
                output_and = g
                if g_next == {"OR"}:
                    g_adder.remove(g)

        # Check output
        checked.add(out)
        if gates[out]["type"] == "XOR" and gates[out]["in"] == {output_in, cin}:
            g_adder.remove(out)

        # Check last two
        remaining = g_adder - checked

        # First check mid AND gate since we need the output for the last step
        mid_and = set(g for g in remaining if gates[g]["type"] == "AND").pop()
        checked.add(mid_and)
        g_next = set(gates[v]["type"] for v in set(get_ins(mid_and)))
        if gates[mid_and]["in"] == {output_in, cin}:
            g_adder.remove(mid_and)

        remaining.remove(mid_and)
        or_out = remaining.pop()
        checked.add(or_out)
        if gates[or_out]["type"] == "OR" and gates[or_out]["in"] == {
            mid_and,
            output_and,
        }:
            g_adder.remove(or_out)

        if g_adder:
            swaps = g_adder
            gate_swap(*g_adder)

        carry = set(g for g in get_all_gates(n, cin) if gates[g]["type"] == "OR").pop()

    return swaps, carry


checked = set()
swaps = {}
carry = None
for n in range(len(xsigs)):
    if n == 14:
        print("stop")
    s, carry = fix_adder(n, carry)
    swaps |= s


# invalid gates
# sgj, z35
# kpp, z31
# vss, z14
# hjf, kdh


part2 = ",".join(sorted([i for pair in invalid for i in pair]))
print(f"Part 2: {part2}")
