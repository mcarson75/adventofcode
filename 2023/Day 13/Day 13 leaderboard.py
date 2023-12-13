with open("input.txt", "r") as f:
    groups = f.read().strip().split("\n\n")


def diff1(a, b):
    return sum([a[i] != b[i] for i in range(len(a))])


part1 = 0
for group in groups:
    lines = group.split("\n")
    refl = False
    for n in range(1, len(lines)):
        if lines[n] == lines[n - 1]:
            refl = True
            rows_to_check = min(n, len(lines) - n)
            for i in range(rows_to_check):
                if not lines[n - i - 1] == lines[n + i]:
                    refl = False
                    break
            if refl:
                part1 += 100 * n
                break
    for n in range(1, len(lines[0])):
        col1 = "".join([l[n - 1] for l in lines])
        col2 = "".join([l[n] for l in lines])
        if col1 == col2:
            refl = True
            cols_to_check = min(n, len(lines[0]) - n)
            for i in range(cols_to_check):
                col1 = "".join([l[n - i - 1] for l in lines])
                col2 = "".join([l[n + i] for l in lines])
                if not col1 == col2:
                    refl = False
                    break
            if refl:
                part1 += n
                break


print(f"Part 1: {part1}")

part2 = 0
for group in groups:
    lines = group.split("\n")
    refl = False
    for n in range(1, len(lines)):
        if lines[n] == lines[n - 1] or diff1(lines[n], lines[n - 1]) == 1:
            refl = True
            rows_to_check = min(n, len(lines) - n)
            diff = 0
            for i in range(rows_to_check):
                diff += diff1(lines[n - i - 1], lines[n + i])
            if diff == 1:
                part2 += 100 * n
                break
    for n in range(1, len(lines[0])):
        col1 = "".join([l[n - 1] for l in lines])
        col2 = "".join([l[n] for l in lines])
        if col1 == col2 or diff1(col1, col2) == 1:
            refl = True
            cols_to_check = min(n, len(lines[0]) - n)
            diff = 0
            for i in range(cols_to_check):
                col1 = "".join([l[n - i - 1] for l in lines])
                col2 = "".join([l[n + i] for l in lines])
                diff += diff1(col1, col2)
            if diff == 1:
                part2 += n
                break

print(f"Part 2: {part2}")
