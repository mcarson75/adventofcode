from collections import defaultdict

secrets = [int(l.strip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]


def get_secret(s):
    for shift in [6, -5, 11]:
        s = mixprune(s, shift)
    return s


mixprune = lambda s, shift: ((s >> -shift if shift < 0 else s << shift) ^ s) & 0xFFFFFF
sequences = defaultdict(int)
part1 = 0

for secret in secrets:
    found_sequences = set()
    s = secret
    price = secret % 10
    deltas = []
    for n in range(2000):
        secret = get_secret(secret)
        deltas.append((new_price := secret % 10) - price)

        if len(deltas) >= 4:
            deltas = deltas[-4:]
            k = tuple(deltas)
            if k not in found_sequences:
                found_sequences.add(k)
                sequences[k] += new_price

        price = new_price
    part1 += secret

part2 = max(sequences.values())

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
