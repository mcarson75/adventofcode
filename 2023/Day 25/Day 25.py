import networkx

lines = [
    l.strip().split(": ") for l in open("input.txt", "r", encoding="utf-8").readlines()
]

G = networkx.Graph()
[G.add_edge(src, tgt) for src, tgts in lines for tgt in tgts.split(" ")]
_, rg = networkx.stoer_wagner(G)

print(f"Part 1: {len(rg[0])*len(rg[1])}")
