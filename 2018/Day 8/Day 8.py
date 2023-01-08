input = [
    int(i)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for i in l.strip().split()
]


def parse(data):
    child, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for _ in range(child):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if child == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:],
        )


total, value, _ = parse(input)

print(f"Part 1: {total}")
print(f"Part 2: {value}")
