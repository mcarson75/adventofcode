with open("input.txt", 'r', encoding='utf-8') as f:
    fish_in = [int(x) for x in f.read().rstrip().split(",")]

fish = [fish_in.count(n) for n in range(9)]

for d in range(256):
    fish.append(fish.pop(0))
    fish[6] += fish[8]

print(sum(fish))
