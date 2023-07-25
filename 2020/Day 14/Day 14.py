lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

mem = {}


def apply_bitmask(mask, input):
    input |= int(mask.replace("X", "0"), 2)
    input &= int(mask.replace("X", "1"), 2)
    return input


def allmasks(pos, mask):
    if not mask:
        yield 0
    else:
        for m in allmasks(pos // 2, mask[:-1]):
            if mask[-1] == "0":
                yield 2 * m + pos % 2
            if mask[-1] == "1":
                yield 2 * m + 1
            if mask[-1] == "X":
                yield 2 * m + 0
                yield 2 * m + 1


mask = None
for line in lines:
    op, value = line.split(" = ")
    if op == "mask":
        mask = value
    else:
        address = int(op[4:-1])
        mem[address] = apply_bitmask(mask, int(value))

part1 = sum(mem.values())

print(f"Part 1: {part1}")

mem = {}
mask = None
for line in lines:
    op, value = line.split(" = ")
    if op == "mask":
        mask = value
    else:
        address = int(op[4:-1])
        for m in allmasks(address, mask):
            mem[m] = int(value)

part2 = sum(mem.values())

print(f"Part 2: {part2}")
