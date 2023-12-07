from functools import cmp_to_key

hands = [l.strip().split(" ") for l in open("input.txt", "r")]
card_order = "_23456789TJQKA"


def card_rank(c, jokers_wild):
    return card_order.index(c) if c != "J" or not jokers_wild else 0


def hand_type(hand, jokers_wild):
    cards = {}
    for c in hand:
        cards[c] = cards.get(c, 0) + 1
    if jokers_wild and "J" in cards and hand != "JJJJJ":
        jokers = cards.pop("J")
        cards[max(cards, key=cards.get)] += jokers

    max_occurrences = max(cards.values())
    unique_cards = len(cards)

    # Full house
    if max_occurrences == 3 and unique_cards == 2:
        return 3.5
    # Two pair
    if max_occurrences == 2 and unique_cards == 3:
        return 2.5
    # All others
    return max_occurrences


def hand(a, b, jokers_wild):
    a, b = a[0], b[0]
    type_diff = hand_type(a, jokers_wild) - hand_type(b, jokers_wild)
    if type_diff:
        return type_diff
    card_diffs = [
        card_rank(a[i], jokers_wild) - card_rank(b[i], jokers_wild)
        for i in range(len(a))
    ]
    return next((diff for diff in card_diffs if diff), 0)


def calculate_score(sorted_hands):
    return sum([(i + 1) * int(v[1]) for i, v in enumerate(sorted_hands)])


part1 = calculate_score(sorted(hands, key=cmp_to_key(lambda a, b: hand(a, b, False))))
part2 = calculate_score(sorted(hands, key=cmp_to_key(lambda a, b: hand(a, b, True))))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
