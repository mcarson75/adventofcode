from collections import deque
from functools import cache


CODES = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

N_PAD = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")],
}
D_PAD = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")],
}
PADS = [N_PAD, D_PAD]


def bfs(u, v, g):
    q = deque([(u, [])])
    seen = {u}
    shortest = None
    res = []
    while q:
        cur, path = q.popleft()
        if cur == v:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                res.append("".join(path + ["A"]))
            continue
        if shortest and len(path) >= shortest:
            continue
        for nei, d in g[cur]:
            seen.add(nei)
            q.append((nei, path + [d]))
    return res


@cache
def dfs(seq, level, i=0):
    g = PADS[i]
    res = 0
    seq = "A" + seq
    for u, v in [(seq[n], seq[n + 1]) for n in range(len(seq) - 1)]:
        paths = bfs(u, v, g)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(dfs(path, level - 1, 1) for path in paths)
    return res


part1 = sum(dfs(code, 2) * int(code[:3]) for code in CODES)
part2 = sum(dfs(code, 25) * int(code[:3]) for code in CODES)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
