from functools import cmp_to_key as cmp

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def compare(l, r):
    for l_, r_ in zip(l, r):
        if type(l_) is int and type(r_) is int:
            if l_ < r_:
                return -1
            elif l_ > r_:
                return 1
        else:
            if type(l_) is int:
                l_ = [l_]
            elif type(r_) is int:
                r_ = [r_]
            c = compare(l_, r_)
            if c:
                return c

    if len(l) < len(r):
        return -1
    elif len(l) > len(r):
        return 1

    return 0


index = 1
part1 = 0
groups = []
for n in range(0, len(lines), 3):
    left = eval(lines[n])
    right = eval(lines[n + 1])
    if compare(left, right) == -1:
        part1 += index
    index += 1

packets = [*map(eval, [l for l in lines if l])] + [[[2]], [[6]]]
sorted_packets = sorted(packets, key=cmp(compare))
part2 = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
