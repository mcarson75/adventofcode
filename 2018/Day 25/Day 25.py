class point:
    def __init__(self, pt):
        self.pos = pt
        self.chain = None

    def __repr__(self):
        return str(self.pos)

    def distance(self, other):
        return sum([abs(self.pos[i] - other.pos[i]) for i in range(len(self.pos))])

    def close(self, other):
        return self.distance(other) <= 3

    def same_chain(self, others):
        return set([pt for pt in others if self.close(pt)])


points = set(
    [
        point([int(i) for i in l.strip().split(",")])
        for l in open("input.txt", "r", encoding="utf-8").readlines()
    ]
)


chain = 1
for pt in points:
    if not pt.chain:
        this_chain = set([pt])
        new_points = set([pt])
        while True:
            new = set()
            for p in new_points:
                new |= p.same_chain(
                    set(p for p in points if not p.chain and p is not pt)
                )
            if not new:
                for c in this_chain:
                    c.chain = chain
                chain += 1
                break
            new_points = new - this_chain
            this_chain |= new


print(f"Part 1: {len(set([p.chain for p in points]))}")
