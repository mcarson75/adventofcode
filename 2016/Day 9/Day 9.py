from itertools import takewhile, islice

text = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

def decompress(data, recurse):
    total = 0
    chars = iter(data)
    for c in chars:
        if c == '(':
            n, m = map(int, [''.join(takewhile(lambda c: c not in 'x)', chars)) for _ in (0, 1)])
            s = ''.join(islice(chars, n))
            total += (decompress(s, recurse) if recurse else len(s)) * m
        else:
            total += 1
    return total

part1 = decompress(text, False)
part2 = decompress(text, True)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))