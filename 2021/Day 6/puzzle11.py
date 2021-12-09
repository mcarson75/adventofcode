with open('input.txt', 'r', encoding='utf-8') as read_file:
    lines = read_file.readlines()

fish = lines[0].rstrip().split(",")
fish = [int(f,10) for f in fish]
#print(len(fish))
print(fish)

days = 80

for d in range(0, days):
    fish = [f-1 for f in fish]
    new_fish = fish.count(-1)
    added_fish = []
    for n in range(0, new_fish):
        added_fish.append(8)
    fish.extend(added_fish)
    #print(new_fish)
    fish = [(6 if h==-1 else h) for h in fish]
    print(d)

print(len(fish))
