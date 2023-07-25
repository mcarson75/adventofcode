numbers = [12, 1, 16, 3, 11, 0]


def do_puzzle(turns, numbers):
    steps, ns = turns, numbers
    last, c = ns[-1], {n: i for i, n in enumerate(ns)}
    for i in range(len(ns) - 1, steps - 1):
        c[last], last = i, i - c.get(last, i)

    return last


print(f"Part 1: {do_puzzle(2020, numbers)}")
print(f"Part 2: {do_puzzle(30000000, numbers)}")
