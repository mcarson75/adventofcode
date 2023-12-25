import networkx

lines = [
    l.strip().split(": ") for l in open("input.txt", "r", encoding="utf-8").readlines()
]

G = networkx.Graph()
for src, tgts in lines:
    for tgt in tgts.split(" "):
        G.add_edge(src, tgt)

cuts = networkx.minimum_edge_cut(G)
G.remove_edges_from(cuts)
rg = list(networkx.connected_components(G))

print(f"Part 1: {len(rg[0])*len(rg[1])}")
