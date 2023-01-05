from collections import defaultdict

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.split() for l in f.readlines()]

lines = [(l[1], l[7]) for l in lines]
steps = set([s[0] for s in lines] + [s[1] for s in lines])


def next(s, l):
    return [s for s in steps if all(b != s for (_, b) in l)]


order = ""
while steps:
    c = next(steps, lines)
    c.sort()

    n = c[0]
    order += n
    steps.remove(n)
    lines = [(a, b) for (a, b) in lines if a != n]

print(f"Part 1: {order}")
