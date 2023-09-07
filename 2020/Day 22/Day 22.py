with open("input.txt") as f:
    chunks = f.read().split("\n\n")

p = [[int(i) for i in c.strip().split("\n")[1:]] for c in chunks]


def score(deck):
    return sum(e * (len(deck) - i) for i, e in enumerate(deck))


# Part 2
def play_game(p1, p2, recurse=True):
    seen1, seen2 = set(), set()

    while len(p1) > 0 and len(p2) > 0:
        if recurse:
            s1 = ",".join([str(c) for c in p1])
            s2 = ",".join([str(c) for c in p2])
            if s1 in seen1 or s2 in seen2:
                return "p1", p1
            seen1.add(s1)
            seen2.add(s2)

        a, b = p1.pop(0), p2.pop(0)
        if a <= len(p1) and b <= len(p2) and recurse:
            winner, _ = play_game(p1.copy()[:a], p2.copy()[:b])
        else:
            if a > b:
                winner = "p1"
            else:
                winner = "p2"

        if winner == "p1":
            p1 += [a, b]
        else:
            p2 += [b, a]

    if len(p1) > 0:
        return "p1", p1
    else:
        return "p2", p2


_, deck = play_game(p[0].copy(), p[1].copy(), recurse=False)
print(f"Part 1: {score(deck)}")

_, deck = play_game(p[0].copy(), p[1].copy(), recurse=True)
print(f"Part 2: {score(deck)}")
