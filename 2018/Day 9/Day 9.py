from collections import deque

last = 70784


def high_score(largest):
    players = [0] * 452
    marbles = deque()
    for marble in range(largest):
        if marble % 23 != 0 or marble == 0:
            marbles.rotate(-1)
            marbles.append(marble)
        else:
            marbles.rotate(7)
            players[marble % len(players)] += marble + marbles.pop()
            marbles.rotate(-1)

    return max(players)


print(f"Part 1: {high_score(last)}")
print(f"Part 2: {high_score(last*100)}")
