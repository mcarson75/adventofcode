lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def run(g, k, s):  # g is grammar, k is a rule, s is a string
    if isinstance(g[k], list):  # an alternative
        yield from run_alt(g, g[k], s)
    else:  # a terminal
        if s and s[0] == g[k]:
            yield s[1:]


def run_alt(g, alt, s):
    for seq in alt:  # try each of the alternatives
        yield from run_seq(g, seq, s)


def run_seq(g, seq, s):
    if not seq:  # an empty sequence matches everything
        yield s
    else:
        k, *seq = seq
        for s in run(g, k, s):  # match current
            yield from run_seq(g, seq, s)  # then match remainder


def match(g, s):
    return any(m == "" for m in run(g, "0", s))


rules = {}
strings = []
for line in lines:
    if ":" in line:
        name, rest = line.split(": ")
        if '"' in rest:
            rules[name] = rest[1:-1]
        else:
            options = rest.split(" | ")
            rules[name] = [x.split(" ") for x in options]
    elif line:
        strings.append(line)


print(f"Part 1: {sum(match(rules, s) for s in strings)}")
rules = {**rules, "8": [["42"], ["42", "8"]], "11": [["42", "31"], ["42", "11", "31"]]}
print(f"Part 2: {sum(match(rules, s) for s in strings)}")
