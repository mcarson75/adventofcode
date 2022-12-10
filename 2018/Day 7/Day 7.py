with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

input = [[l.split()[1], l.split()[7]] for l in lines]

tree = {}


def reduce_tree(tree):
    new_tree = {}
    c = set([i for s in tree.values() for i in s])
    p = set([i for s in tree.keys() for i in s])
    for k in p.difference(c):
        new_tree[k] = []
        for i in tree[k]:
            new_tree[k].append({i: tree[i]})


for p, c in input:
    tree[p] = tree.get(p, []) + [c]

reduce_tree(tree)

print("stop")
