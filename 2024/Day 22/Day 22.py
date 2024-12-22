from collections import defaultdict

secrets = [int(l.strip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]

mixprune = lambda s, shift: ((s >> -shift if shift < 0 else s << shift) ^ s) & 0xFFFFFF


def get_secret(s):
    for shift in [6, -5, 11]:
        s = mixprune(s, shift)
    return s


sequences = defaultdict(int)
part1 = 0

for secret in secrets:
    found_sequences = set()
    s = secret
    p1 = secret % 10
    deltas = []
    for n in range(2000):
        secret = get_secret(secret)
        p2 = secret % 10
        deltas.append(p2 - p1)

        if len(deltas) >= 4:
            deltas = deltas[-4:]
            k = tuple(deltas)
            if k not in found_sequences:
                found_sequences.add(k)
                sequences[k] += p2

        p1 = p2
    part1 += secret

part2 = max(sequences.values())

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
