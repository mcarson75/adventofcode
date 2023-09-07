lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def get_coord(line):
    pos = 0
    while line:
        if line[0] == "e":
            pos += 2
            line = line[1:]
        elif line[0] == "w":
            pos += -2
            line = line[1:]
        elif line[:2] == "se":
            pos += 1 - 1j
            line = line[2:]
        elif line[:2] == "sw":
            pos += -1 - 1j
            line = line[2:]
        elif line[:2] == "ne":
            pos += 1 + 1j
            line = line[2:]
        elif line[:2] == "nw":
            pos += -1 + 1j
            line = line[2:]

    return pos


def get_surr(coord):
    return set(
        [
            coord + 2,
            coord - 2,
            coord + 1 - 1j,
            coord - 1 - 1j,
            coord + 1 + 1j,
            coord - 1 + 1j,
        ]
    )


def get_black(tiles, coord):
    return len(get_surr(coord) & tiles)


tiles = set()
for line in lines:
    pos = get_coord(line)
    if pos in tiles:
        tiles.remove(pos)
    else:
        tiles.add(pos)

print(f"Part 1: {len(tiles)}")

for _ in range(100):
    new_tiles = set()
    for t in tiles:
        if get_black(tiles, t) in [1, 2]:
            new_tiles.add(t)
        for s in get_surr(t):
            if s not in tiles and get_black(tiles, s) == 2:
                new_tiles.add(s)

    tiles = new_tiles

print(f"Part 2: {len(tiles)}")
