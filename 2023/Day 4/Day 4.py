lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

part1 = 0
part2 = 0
card_scores = dict()
card_quan = dict()

for line in lines:
    card, game = line.split(":")
    card = int(card[5:])
    winning, drawn = game.split("|")
    winning = set([int(i) for i in winning.split()])
    drawn = set([int(i) for i in drawn.split()])

    winners = len(winning & drawn)
    card_scores[card] = winners
    if winners > 0:
        part1 += 2 ** (winners - 1)

for card in card_scores:
    if card in card_quan:
        card_quan[card] += 1
    else:
        card_quan[card] = 1
    for _ in range(card_quan[card]):
        for i in range(1, card_scores[card] + 1):
            if card + i in card_quan:
                card_quan[card + i] += 1
            else:
                card_quan[card + i] = 1

part2 = sum(card_quan.values())

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
