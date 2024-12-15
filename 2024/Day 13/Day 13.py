import re

CONVERSION = 10000000000000
cplx = lambda a: a[0] + a[1] * 1j

input = [l.rstrip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
machines = [cplx([int(i) for i in re.findall(r"\d+", line)]) for line in input if line]
machines = [machines[n : n + 3] for n in range(0, len(machines), 3)]


def score(machine, conversion):
    a, b, prize = machine
    prize += conversion * (CONVERSION + CONVERSION * 1j)

    na = (b.imag * prize.real - b.real * prize.imag) // (
        a.real * b.imag - b.real * a.imag
    )

    nb = (prize.imag - a.imag * na) // b.imag

    if na * a + nb * b != prize or (not conversion and (na > 100 or nb > 100)):
        return 0

    return int(na * 3 + nb)


part1 = sum([score(machine, False) for machine in machines])
part2 = sum([score(machine, True) for machine in machines])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
