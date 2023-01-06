from collections import defaultdict

input = [
    l.strip().split() for l in open("input.txt", "r", encoding="utf-8").readlines()
]

lines = [(l[1], l[7]) for l in input]
steps = set([s[0] for s in lines] + [s[1] for s in lines])

next = lambda s, l: sorted([s for s in steps if all(b != s for (_, b) in l)])

order = ""
while steps:
    c = next(steps, lines)
    n = c[0]

    order += n
    steps.remove(n)
    lines = [(a, b) for (a, b) in lines if a != n]

print(f"Part 1: {order}")


lines = [(l[1], l[7]) for l in input]
steps = set([s[0] for s in lines] + [s[1] for s in lines])
queue = [("", 0)] * 5
time = 0

while steps or any([q[1] > 0 for q in queue]):
    c = next(steps, lines)
    for q in range(len(queue)):
        queue[q] = (queue[q][0], max(queue[q][1] - 1, 0))
        s, t = queue[q]
        if t == 0:
            if s:
                lines = [(a, b) for (a, b) in lines if a != s]
            if c:
                s = c.pop(0)
                t = ord(s) - 5
                queue[q] = (s, t)
                steps.remove(s)

    time += 1

print(f"Part 2: {time}")
