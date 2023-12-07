from functools import cmp_to_key

hands = [l.strip().split(" ") for l in open("input.txt", "r")]
jokers_wild = False
card_order = "_23456789TJQKA"


def CardRank(c):
    if c == "J" and jokers_wild:
        return 0
    return card_order.index(c)


def HandType(hand):
    cards = {}
    for c in hand:
        cards[c] = cards.get(c, 0) + 1
    if jokers_wild and "J" in cards and hand != "JJJJJ":
        jokers = cards.pop("J")
        cards[max(cards, key=cards.get)] += jokers
    if max(cards.values()) == 5:
        return 6
    if max(cards.values()) == 4:
        return 5
    if max(cards.values()) == 3 and len(cards.keys()) == 2:
        return 4
    if max(cards.values()) == 3:
        return 3
    if max(cards.values()) == 2 and len(cards.keys()) == 3:
        return 2
    if max(cards.values()) == 2:
        return 1
    return 0


def Hand(a, b):
    a, b = a[0], b[0]
    TypeDiff = HandType(a) - HandType(b)
    if TypeDiff:
        return TypeDiff
    for i in range(len(a)):
        CardDiff = CardRank(a[i]) - CardRank(b[i])
        if CardDiff:
            return CardDiff
    return 0


hands.sort(key=cmp_to_key(Hand))
part1 = sum([(i + 1) * int(v[1]) for i, v in enumerate(hands)])

jokers_wild = True
hands.sort(key=cmp_to_key(Hand))
part2 = sum([(i + 1) * int(v[1]) for i, v in enumerate(hands)])


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
