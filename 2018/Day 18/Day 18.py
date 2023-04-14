lines = [
    [x for x in l.strip()] for l in open("input.txt", "r", encoding="utf-8").readlines()
]

input = {}

for y in range(len(lines)):
    for x in range(len(lines[y])):
        input[x + y * 1j] = lines[y][x]

acres = []
acres.append(input)


def do_magic(acres):
    new = {}
    for acre in acres:
        surrounding = ""
        for x in [-1, 0, 1]:
            for y in [-1j, 0, 1j]:
                if not (x == 0 and y == 0):
                    if acre + x + y in acres:
                        surrounding += acres[acre + x + y]
        if acres[acre] == "." and surrounding.count("|") >= 3:
            new[acre] = "|"
        elif acres[acre] == "|" and surrounding.count("#") >= 3:
            new[acre] = "#"
        elif acres[acre] == "#" and not (
            surrounding.count("#") >= 1 and surrounding.count("|") >= 1
        ):
            new[acre] = "."
        else:
            new[acre] = acres[acre]
    return new


def resource_value(acres, index):
    woods = len([a for a in acres[index].values() if a == "|"])
    lumberyards = len([a for a in acres[index].values() if a == "#"])

    return woods * lumberyards


while True:
    new = do_magic(acres[-1])
    if new not in acres:
        acres.append(new)
    else:
        first = acres.index(new)
        break

print(f"Part 1: {resource_value(acres,10)}")

index = (1000000000 - first) % (len(acres) - first) + first
print(f"Part 2: {resource_value(acres,index)}")
