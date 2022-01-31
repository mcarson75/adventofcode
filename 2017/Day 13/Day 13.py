lines = [l.strip().split(': ') for l in open("input.txt", 'r', encoding='utf-8').readlines()]

heights = {int(k): int(v) for k, v in lines}
def severity():
    return sum([d * w for d, w in heights.items() if d % (2 * (w - 1)) == 0])

def caught(delay = 0):
    for d in heights.keys():   # Do this loop instead of list comprehension so it can break out as soon as it finds a True instead of calculating all
        if (d + delay) % (2 * (heights[d] - 1)) == 0:
            return True
    return False

part1 = severity()
part2 = 0
while caught(part2) > 0:
    part2 += 1

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))