cards = [l.strip().split(":")[1] for l in open("input.txt", "r")]

part1 = 0
num_cards = [1] * len(cards)

for i, game in enumerate(cards):
    winning, drawn = game.split("|")
    winning = set(winning.split())
    drawn = set(drawn.split())

    winners = len(winning & drawn)
    if winners:
        part1 += 2 ** (winners - 1)
        for index in range(1, winners + 1):
            num_cards[i + index] += num_cards[i]

part2 = sum(num_cards)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
