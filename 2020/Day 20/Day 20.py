lines = [l.strip() for l in open("input_test.txt", "r", encoding="utf-8").readlines()]

tiles = {}
all_edges = {}


class tile:
    def __init__(self, gr, num):
        self.a = self.get_id(gr[0]) ** 2 + self.get_id(gr[0][::-1]) ** 2
        self.b = self.get_id(gr[-1]) ** 2 + self.get_id(gr[-1][::-1]) ** 2
        self.c = (
            self.get_id("".join([g[0] for g in gr])) ** 2
            + self.get_id("".join([g[0] for g in gr])[::-1]) ** 2
        )
        self.d = (
            self.get_id("".join([g[-1] for g in gr])) ** 2
            + self.get_id("".join([g[-1] for g in gr])[::-1]) ** 2
        )

        self.edges = [self.a, self.b, self.c, self.d]
        for e in self.edges:
            if e in all_edges:
                all_edges[e] += 1
            else:
                all_edges[e] = 1
        self.num = num

    def __repr__(self):
        return self.num

    def get_id(self, s):
        s = s.replace("#", "1").replace(".", "0")
        return int(s, 2)

    def get_unique_edges(self):
        unique = [e for e in self.edges if all_edges[e] == 1]
        return len(unique)

    @property
    def is_corner(self):
        return self.get_unique_edges() == 2


tile_number = None
grid = []
for line in lines:
    if "Tile" in line:
        text, t = line.split(" ")
        tile_number = int(t[:-1])
    elif not line:
        tiles[tile_number] = tile(grid, tile_number)
        grid = []
    else:
        grid.append(line)

if grid:
    tiles[tile_number] = tile(grid, tile_number)

corners = [t for t, v in tiles.items() if v.is_corner]
part1 = 1
for c in corners:
    part1 *= c

print(f"{len(corners)} corners found")
print(f"Corners: {corners}")
print(f"Part 1: {part1}")
