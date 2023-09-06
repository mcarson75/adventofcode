keys = [int(l.strip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]


def do_transform(num, subj):
    return (subj * num) % 20201227


def loop_size(key):
    loop = 1
    num = 7
    while num != key:
        num = do_transform(num, 7)
        loop += 1

    return loop


loops = []
for key in keys:
    loops.append(loop_size(key))

subj = keys[0]
part1 = 1
for _ in range(loops[1]):
    part1 = do_transform(part1, subj)

print(f"Part 1: {part1}")
