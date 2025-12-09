from itertools import combinations

tiles = [
    tuple(int(i) for i in l.strip("\n").split(","))
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]

area = lambda a, b: (abs(a[1] - b[1]) + 1) * (abs(a[0] - b[0]) + 1)


def inside(point, vertical_edges):
    in_polygon = False
    for xe, y1, y2 in vertical_edges:
        if y1 <= point[1] < y2 and xe < point[0]:
            in_polygon = not in_polygon
    return in_polygon


def boundaries(a, b):
    x_min, x_max = sorted((a[0], b[0]))
    y_min, y_max = sorted((a[1], b[1]))
    corners = set([(x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max)])

    return corners, x_min, x_max, y_min, y_max


def is_valid(a, b, tiles, vert, horz):
    corners, x_min, x_max, y_min, y_max = boundaries(a, b)
    for corner in corners - tiles:
        if not inside(corner, vert):
            return False

    for ye, x0, x1 in horz:
        if y_min < ye < y_max:
            if not (x1 <= x_min or x0 >= x_max):
                return False

    for xe, y0, y1 in vert:
        if x_min < xe < x_max:
            if not (y1 <= y_min or y0 >= y_max):
                return False

    return True


edges = list(zip(tiles, tiles[1:] + [tiles[0]]))
vertical_edges = [(x0, *sorted((y0, y1))) for (x0, y0), (x1, y1) in edges if x0 == x1]
horizontal_edges = [(y0, *sorted((x0, x1))) for (x0, y0), (x1, y1) in edges if y0 == y1]

part1 = max(area(a, b) for a, b in combinations(set(tiles), 2))

part2 = 0
for a, b in combinations(set(tiles), 2):
    if is_valid(a, b, set(tiles), vertical_edges, horizontal_edges):
        part2 = max(part2, area(a, b))


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
