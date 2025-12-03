ranges = [
    m.split("-")
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for m in l.strip().split(",")
]

inrange = lambda x, r: x in range(int(r[0]), int(r[1]) + 1)


def find_invalid(rang, mult):
    ans = set()
    lens = [len(i) for i in rang]
    if not lens[0] % mult:
        st = rang[0][: lens[0] // mult]
    elif not lens[1] % mult:
        st = "1" + "0" * (lens[1] // mult - 1)
    else:
        st = ""
    if st:
        length = len(st)
        while len(st) == length:
            test = int(st * mult)
            if inrange(test, rang):
                ans.add(test)
            elif test > int(rang[1]):
                break
            st = str(int(st) + 1)
    return ans


part1 = set()
part2 = set()
for rang in ranges:
    for mult in range(2, len(rang[1]) + 1):
        if any([len(r) % mult == 0 for r in rang]):
            res = find_invalid(rang, mult)
            part2 |= res
            if mult == 2:
                part1 |= res

print(f"Part 1: {sum(part1)}")
print(f"Part 2: {sum(part2)}")
