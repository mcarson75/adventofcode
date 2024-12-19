lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

c1 = int(lines[8].split(" ")[1])
c2 = int(lines[12].split(" ")[2])


def run(c1, c2):
    seen = set()
    c = 0
    part1 = None
    last_unique = None

    while True:
        a = c | 65536
        c = c1

        while True:
            c = (((c + (a & 255)) & 16777215) * c2) & 16777215

            if a < 256:
                if not part1:
                    part1 = c
                if c not in seen:
                    seen.add(c)
                    last_unique = c
                    break
                else:
                    return part1, last_unique
            else:
                a //= 256


part1, part2 = run(c1, c2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
