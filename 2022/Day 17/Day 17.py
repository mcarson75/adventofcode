lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]
moves = [1 if i == ">" else -1 for i in lines[0]]

shapes = (
    (0, 1, 2, 3),
    (1, 1j, 1 + 1j, 2 + 1j, 1 + 2j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 1j, 2j, 3j),
    (0, 1, 1j, 1 + 1j),
)


def rock_fall(rocks, m, r, height, num_rocks):
    height_to_store = 32

    for r in range(num_rocks):
        rock = shapes[r % len(shapes)]
        rock = set(i + 2 + (height + 4) * 1j for i in rock)
        while True:
            move = moves[m % len(moves)]
            m += 1

            new_rock = {i + move for i in rock}
            if any(z.real < 0 or z.real >= 7 for z in new_rock):
                new_rock = rock
            if any(r in rocks for r in new_rock):
                new_rock = rock
            rock = new_rock

            new_rock = {i - 1j for i in rock}
            if any(r in rocks for r in new_rock):
                rocks = rocks | rock
                height = int(max([z.imag for z in rocks]))
                rocks = set(i for i in rocks if i.imag >= height - height_to_store)
                if height - height_to_store - 1 > 0:
                    rocks = rocks | {
                        x + (height - height_to_store - 1) * 1j for x in range(7)
                    }
                break

            rock = new_rock

    return rocks, m, height


def part1():
    rocks = {x + 0j for x in range(7)}
    _, _, height = rock_fall(rocks, 0, 0, 0, 2022)

    return height


print(f"Part 1: {part1()}")


def part2():
    rocks = {x + 0j for x in range(7)}
    total_rocks = 1000000000000

    m, r, h = 0, 0, 0

    signatures = {}
    while r < total_rocks:
        rocks, m, h = rock_fall(rocks, m, r, h, len(shapes))
        r += len(shapes)
        min_height = min(z.imag for z in rocks) * 1j
        sig = tuple(
            sorted([r - min_height for r in rocks], key=lambda z: (z.imag, z.real))
        )
        if sig in signatures:
            last_m, last_r, last_h = signatures[sig]
            if last_m % len(moves) == m % len(moves):
                reps = (total_rocks - r) // (r - last_r)
                h += reps * (h - last_h)
                r += reps * (r - last_r)
                rocks = {i + (h - max(z.imag for z in rocks)) * 1j for i in rocks}
        signatures[sig] = (m, r, h)

    return h


print(f"Part 2: {part2()}")
