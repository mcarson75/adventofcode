readings = [
    [int(i) for i in l.strip().split()]
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]


def calc_next(seq):
    seqs = [seq]
    while not all([s == 0 for s in seqs[-1]]):
        seqs.append([b - a for a, b in zip(seqs[-1][:-1], seqs[-1][1:])])
    for n in range(len(seqs) - 1, 0, -1):
        seqs[n - 1].append(seqs[n - 1][-1] + seqs[n][-1])
    return seqs[0][-1]


part1 = sum([calc_next(r) for r in readings])
part2 = sum([calc_next(r[::-1]) for r in readings])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
