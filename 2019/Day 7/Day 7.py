import intcode
from itertools import permutations

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

out_signal = 0

for perm in permutations([0, 1, 2, 3, 4]):
    out = 0
    for p in perm:
        out = intcode.run(code, input=out, phase=p)
    out_signal = max(out, out_signal)

print(f"Part 1: {out_signal}")
