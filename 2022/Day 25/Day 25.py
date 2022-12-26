lines = [l.rstrip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def snafu_to_dec(s):
    map = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}

    s = [map[i] for i in s[::-1]]
    return int(sum([5**i * s[i] for i in range(len(s))]))


def dec_to_snafu(d):
    map = {3: "=", 4: "-", 5: 0}

    s = []
    while d:
        s += [d % 5]
        d //= 5

    for n in range(len(s)):
        if s[n] in map.keys():
            s[n] = map[s[n]]
            s[n + 1] += 1

    return "".join([str(c) for c in s[::-1]])


total = int(sum([snafu_to_dec(l) for l in lines]))
part1 = dec_to_snafu(total)
print(f"Part 1: {part1}")
