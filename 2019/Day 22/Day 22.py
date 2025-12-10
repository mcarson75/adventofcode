shuffles = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

DECK_SIZE_PT1 = 10007
CARD_PT1 = 2019

DECK_SIZE_PT2 = 119315717514047
POSITION_PT2 = 2020
SHUFFLES_PT2 = 101741582076661


def get_card(deck_size, position, reps):
    def parse():
        a, b = 1, 0
        for shuffle in shuffles[::-1]:
            if shuffle == "deal into new stack":
                a = -a
                b = deck_size - b - 1
            elif "cut" in shuffle:
                num = int(shuffle.split()[1])
                b = (b + num) % deck_size
            elif "deal with increment" in shuffle:
                num = int(shuffle.split()[-1])
                z = pow(num, deck_size - 2, deck_size)
                a = a * z % deck_size
                b = b * z % deck_size
        return a, b

    def polypow(a, b, m, n):
        if m == 0:
            return 1, 0
        if m % 2 == 0:
            return polypow(a * a % n, (a * b + b) % n, m // 2, n)
        else:
            c, d = polypow(a, b, m - 1, n)
            return a * c % n, (a * d + b) % n

    a, b = polypow(*parse(), reps, deck_size)

    return (position * a + b) % deck_size


deck = [get_card(DECK_SIZE_PT1, d, 1) for d in range(DECK_SIZE_PT1)]
part1 = deck.index(CARD_PT1)

part2 = get_card(DECK_SIZE_PT2, POSITION_PT2, SHUFFLES_PT2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
