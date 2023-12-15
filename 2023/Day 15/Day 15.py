import re

pattern = r"([a-z]+)(?:-|=)(\d+)?"
input = open("input.txt").read().strip()
strings = re.findall(pattern, input)
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


def get_focus(box):
    power = sum([(i + 1) * p[1] for (i, p) in enumerate(boxes[box])])
    return (box + 1) * power


for label, power in strings:
    if power:
        power = int(power)
    box = hash(label)
    index = get_lens(label, boxes[box])
    if not power and index >= 0:
        del boxes[box][index]
    elif index >= 0:
        boxes[box][index] = (label, power)
    elif power:
        boxes[box].append((label, power))

part1 = sum([hash(string) for string in input.split(",")])
part2 = sum([get_focus(box) for box in boxes])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
