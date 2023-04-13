import numpy as np

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

clay = set()
water = set()
falling = set()
settled = set()

for line in lines:
    for c in line.split(", "):
        axis, coord = c.split("=")
        if ".." in coord:
            start, stop = [int(i) for i in coord.split("..")]
        else:
            start = stop = int(coord)
        if axis == "x":
            xrange = range(start, stop + 1)
        else:
            yrange = range(start, stop + 1)
    for x in xrange:
        for y in yrange:
            clay.add(x + y * 1j)

top = min([c.imag for c in clay])
bottom = max([c.imag for c in clay])


def printout(clay):
    file = open("output.txt", "w")
    xmin = min([int(c.real) for c in clay])
    xmax = max([int(c.real) for c in clay])
    ymax = max([int(c.imag) for c in clay])
    output = np.full((ymax + 1, xmax - xmin + 5), " ")
    for y in range(ymax + 1):
        for x in range(xmin - 2, xmax + 3):
            if x + y * 1j == 500:
                output[y, x - xmin + 2] = "x"
            elif x + y * 1j in clay:
                output[y, x - xmin + 2] = "#"
            elif x + y * 1j in settled:
                output[y, x - xmin + 2] = "~"
            elif x + y * 1j in falling:
                output[y, x - xmin + 2] = "|"
            elif x + y * 1j in water:
                output[y, x - xmin + 2] = "|"
            elif x + y * 1j in streams:
                output[y, x - xmin + 2] = "|"
        print("".join(output[y]), file=file)
    file.close()


def resolve_stream(stream):
    falling.add(stream)
    if stream + 1 in water and stream - 1 in water:
        return
    while stream + 1j not in clay | water:
        stream += 1j
        if stream.imag > bottom:
            return
        falling.add(stream)
    else:
        # doprint()
        if stream + 1j in water:
            stream += 1j
        water.add(stream)
        while flow_lr(stream):
            stream -= 1j
        return


def flow_lr(stream):
    global settled

    water.add(stream)
    l, settled_l = flow(stream, -1)
    r, settled_r = flow(stream, 1)
    if not l and not r:
        settled |= settled_r | settled_l
    return not l and not r


def flow(pos, dir):
    settle = set()
    settle.add(pos)
    while True:
        pos += dir
        if pos not in clay and pos + 1j in clay | water:
            water.add(pos)
            settle.add(pos)
        elif pos in clay:
            return False, settle
        elif pos + 1j not in clay | water:
            if pos not in streams:
                streams.append(pos)
            return True, set()


streams = [500]
while streams:
    stream = streams.pop(0)
    resolve_stream(stream)

printout(clay)
part1 = len({w for w in water | falling if top <= w.imag <= bottom})
part2 = len(settled)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
