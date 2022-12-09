import numpy as np

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]


def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


def ropeMove(lines, numKnots):
    visited = set()
    k = np.array([[0, 0] for i in range(numKnots)])
    visited = {tuple(k[-1])}

    for line in lines:
        dir, move = line.split()

        for _ in range(int(move)):
            if dir == "L":
                k[0, 0] -= 1
            elif dir == "R":
                k[0, 0] += 1
            if dir == "D":
                k[0, 1] -= 1
            elif dir == "U":
                k[0, 1] += 1

            for n in range(1, len(k)):
                dx, dy = k[n - 1, 0] - k[n, 0], k[n - 1, 1] - k[n, 1]
                if abs(dx) > 1 or abs(dy) > 1:
                    k[n, 0] += sign(dx)
                    k[n, 1] += sign(dy)
            visited.add(tuple(k[-1]))
    return len(visited)


print(f"Part 1: {ropeMove(lines, 2)}")
print(f"Part 2: {ropeMove(lines, 10)}")
