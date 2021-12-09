from timeit import default_timer as timer

with open("input.txt", 'r', encoding='utf-8') as f:
    fish_in = [int(x) for x in f.read().rstrip().split(",")]

start = timer()

fish = [fish_in.count(n) for n in range(9)]

for d in range(256):
    fish.append(fish.pop(0))
    fish[6] += fish[8]

end = timer()

print(sum(fish))
print(f"{end-start} seconds")
