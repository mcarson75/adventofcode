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
        seqs[n - 1].insert(0, seqs[n - 1][0] - seqs[n][0])
    return (seqs[0][-1], seqs[0][0])


next_values = [calc_next(r) for r in readings]
part1 = sum([v[0] for v in next_values])
part2 = sum([v[1] for v in next_values])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
