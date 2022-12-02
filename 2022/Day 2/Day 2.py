game = dict()
game["A X"] = (1 + 3, 0 + 3)
game["A Y"] = (2 + 6, 3 + 1)
game["A Z"] = (3 + 0, 6 + 2)
game["B X"] = (1 + 0, 0 + 1)
game["B Y"] = (2 + 3, 3 + 2)
game["B Z"] = (3 + 6, 6 + 3)
game["C X"] = (1 + 6, 0 + 2)
game["C Y"] = (2 + 0, 3 + 3)
game["C Z"] = (3 + 3, 6 + 1)

score = [0, 0]

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

for k in game.keys():
    for i in range(len(score)):
        score[i] += lines.count(k) * game[k][i]

print(f"Part 1: {score[0]}")
print(f"Part 2: {score[1]}")
