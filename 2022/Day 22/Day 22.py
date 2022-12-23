import re

lines = [l.rstrip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

instructions = lines[-1]
lines = lines[:-2]
map = set()
wall = set()

instructions = re.findall("\d+|L|R", instructions)
instructions = [int(i) if i.isdigit() else i for i in instructions]

for row in range(1, len(lines) + 1):
    line = lines[row - 1]
    for col in range(1, len(line) + 1):
        c = line[col - 1]
        if c == "." or c == "#":
            map.add((col, row))
        if c == "#":
            wall.add((col, row))


def this_row(s, r):
    return list(m[0] for m in s if m[1] == r)


def this_col(s, c):
    return list(m[1] for m in s if m[0] == c)


def do_moves(maptype="flat"):
    pos = (min(this_row(map, 1)), 1)
    face = "r"

    dir = {"r": (1, 0), "l": (-1, 0), "u": (0, -1), "d": (0, 1)}
    dirs = ["r", "d", "l", "u"]

    edge1a = tuple((51, 50 + i) for i in range(1, 51))  # vertical, x=51, y= 51-100
    edge1b = tuple((i, 101) for i in range(1, 51))  # horizontal,   x = 51-100, y=101

    edge2a = tuple((50, 150 + i) for i in range(1, 51))  # vertical
    edge2b = tuple((i + 50, 150) for i in range(1, 51))  # horizontal

    edge3a = tuple((100, 50 + i) for i in range(1, 51))  # vertical
    edge3b = tuple((i + 100, 50) for i in range(1, 51))  # horizontal

    edge4a = tuple((51, i) for i in range(1, 51))  # vertical
    edge4b = tuple((1, i + 100) for i in range(50, 0, -1))  # vertical

    edge5a = tuple((1, 150 + i) for i in range(1, 51))  # vertical
    edge5b = tuple((i + 50, 1) for i in range(1, 51))  # horizontal

    edge6a = tuple((100, 100 + i) for i in range(1, 51))  # vertical
    edge6b = tuple((150, i) for i in range(50, 0, -1))  # vertical

    edge7a = tuple((i, 200) for i in range(1, 51))  # horizontal
    edge7b = tuple((i + 100, 1) for i in range(1, 51))  # horizontal

    for move in instructions:
        if type(move) is int:
            for _ in range(move):
                next_pos = (pos[0] + dir[face][0], pos[1] + dir[face][1])
                next_face = face
                if next_pos not in map and maptype == "flat":
                    if face == "r":
                        next_pos = (min(this_row(map, pos[1])), pos[1])
                    elif face == "l":
                        next_pos = (max(this_row(map, pos[1])), pos[1])
                    elif face == "u":
                        next_pos = (pos[0], max(this_col(map, pos[0])))
                    elif face == "d":
                        next_pos = (pos[0], min(this_col(map, pos[0])))
                elif next_pos not in map and maptype == "cube":
                    if pos in edge1a and face == "l":
                        i = edge1a.index(pos)
                        next_pos = edge1b[i]
                        next_face = "d"
                    elif pos in edge1b and face == "u":
                        i = edge1b.index(pos)
                        next_pos = edge1a[i]
                        next_face = "r"

                    elif pos in edge2a and face == "r":
                        i = edge2a.index(pos)
                        next_pos = edge2b[i]
                        next_face = "u"
                    elif pos in edge2b and face == "d":
                        i = edge2b.index(pos)
                        next_pos = edge2a[i]
                        next_face = "l"

                    elif pos in edge3a and face == "r":
                        i = edge3a.index(pos)
                        next_pos = edge3b[i]
                        next_face = "u"
                    elif pos in edge3b and face == "d":
                        i = edge3b.index(pos)
                        next_pos = edge3a[i]
                        next_face = "l"

                    elif pos in edge4a and face == "l":
                        i = edge4a.index(pos)
                        next_pos = edge4b[i]
                        next_face = "r"
                    elif pos in edge4b and face == "l":
                        i = edge4b.index(pos)
                        next_pos = edge4a[i]
                        next_face = "r"

                    elif pos in edge5a and face == "l":
                        i = edge5a.index(pos)
                        next_pos = edge5b[i]
                        next_face = "d"
                    elif pos in edge5b and face == "u":
                        i = edge5b.index(pos)
                        next_pos = edge5a[i]
                        next_face = "r"

                    elif pos in edge6a and face == "r":
                        i = edge6a.index(pos)
                        next_pos = edge6b[i]
                        next_face = "l"
                    elif pos in edge6b and face == "r":
                        i = edge6b.index(pos)
                        next_pos = edge6a[i]
                        next_face = "l"

                    elif pos in edge7a and face == "d":
                        i = edge7a.index(pos)
                        next_pos = edge7b[i]
                        next_face = "d"
                    elif pos in edge7b and face == "u":
                        i = edge7b.index(pos)
                        next_pos = edge7a[i]
                        next_face = "u"

                if next_pos in wall:
                    break
                pos = next_pos
                face = next_face

        else:
            face = dirs[(dirs.index(face) + (1 if move == "R" else -1)) % 4]

    return 1000 * pos[1] + 4 * pos[0] + dirs.index(face)


print(f"Part 1: {do_moves('flat')}")
print(f"Part 2: {do_moves('cube')}")
