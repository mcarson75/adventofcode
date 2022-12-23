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

    edges = [
        {
            "a": {
                "range": tuple((51, 50 + i) for i in range(1, 51)),
                "from": "l",
                "to": "d",
            },
            "b": {
                "range": tuple((i, 101) for i in range(1, 51)),
                "from": "u",
                "to": "r",
            },
        },
        {
            "a": {
                "range": tuple((50, 150 + i) for i in range(1, 51)),
                "from": "r",
                "to": "u",
            },
            "b": {
                "range": tuple((i + 50, 150) for i in range(1, 51)),
                "from": "d",
                "to": "l",
            },
        },
        {
            "a": {
                "range": tuple((100, 50 + i) for i in range(1, 51)),
                "from": "r",
                "to": "u",
            },
            "b": {
                "range": tuple((i + 100, 50) for i in range(1, 51)),
                "from": "d",
                "to": "l",
            },
        },
        {
            "a": {
                "range": tuple((51, i) for i in range(1, 51)),
                "from": "l",
                "to": "r",
            },
            "b": {
                "range": tuple((1, i + 100) for i in range(50, 0, -1)),
                "from": "l",
                "to": "r",
            },
        },
        {
            "a": {
                "range": tuple((1, 150 + i) for i in range(1, 51)),
                "from": "l",
                "to": "d",
            },
            "b": {
                "range": tuple((i + 50, 1) for i in range(1, 51)),
                "from": "u",
                "to": "r",
            },
        },
        {
            "a": {
                "range": tuple((100, 100 + i) for i in range(1, 51)),
                "from": "r",
                "to": "l",
            },
            "b": {
                "range": tuple((150, i) for i in range(50, 0, -1)),
                "from": "r",
                "to": "l",
            },
        },
        {
            "a": {
                "range": tuple((i, 200) for i in range(1, 51)),
                "from": "d",
                "to": "d",
            },
            "b": {
                "range": tuple((i + 100, 1) for i in range(1, 51)),
                "from": "u",
                "to": "u",
            },
        },
    ]

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
                    for edge in edges:
                        for r in edge:
                            this = edge[r]
                            that = edge["a" if r == "b" else "b"]
                            if pos in this["range"] and face == this["from"]:
                                i = this["range"].index(pos)
                                next_face = this["to"]
                                next_pos = that["range"][i]

                if next_pos in wall:
                    break
                pos = next_pos
                face = next_face

        else:
            face = dirs[(dirs.index(face) + (1 if move == "R" else -1)) % 4]

    return 1000 * pos[1] + 4 * pos[0] + dirs.index(face)


print(f"Part 1: {do_moves('flat')}")
print(f"Part 2: {do_moves('cube')}")
