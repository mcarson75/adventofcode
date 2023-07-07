input = range(138241, 674034 + 1)


def any_adjacent(num):
    return any([j == i for i, j in zip(num[:-1], num[1:])])


def strict_adjacent(num):
    adj = [j == i for i, j in zip(num[:-1], num[1:])]
    for i in range(len(adj)):
        if i == 0 and adj[i] and not adj[i + 1]:
            return True
        elif i == len(adj) - 1 and adj[i] and not adj[i - 1]:
            return True
        elif adj[i] and not adj[i - 1] and not adj[i + 1]:
            return True
    return False


def never_decreasing(num):
    diff = [j - i for i, j in zip(num[:-1], num[1:])]
    return all([d >= 0 for d in diff])


matches = 0
matches_strict = 0
for i in input:
    num = [int(n) for n in list(str(i))]
    if any_adjacent(num) and never_decreasing(num):
        matches += 1
    if strict_adjacent(num) and never_decreasing(num):
        matches_strict += 1

print(f"Part 1: {matches}")
print(f"Part 2: {matches_strict}")
