strings = [l.strip().split(",") for l in open("input.txt", "r")][0]

boxes = {k: [] for k in range(256)}


def hash(string):
    h = 0
    for s in string:
        h += ord(s)
        h *= 17
        h %= 256
    return h


def get_lens(label, lenses):
    labels = [l[0] for l in lenses]
    if label in labels:
        return labels.index(label)
    return -1


part1 = sum([hash(string) for string in strings])

print(f"Part 1: {part1}")

for string in strings:
    if "-" in string:
        label, _ = string.split("-")
        power = None
    else:
        label, power = string.split("=")
        power = int(power)
    box = hash(label)
    index = get_lens(label, boxes[box])
    if not power and index >= 0:
        del boxes[box][index]
    elif index >= 0:
        boxes[box][index] = (label, power)
    elif power:
        boxes[box].append((label, power))

part2 = sum(
    [
        sum([(box + 1) * (i + 1) * boxes[box][i][1] for i in range(len(boxes[box]))])
        for box in boxes
    ]
)


print(f"Part 2: {part2}")
