with open("input.txt", 'r', encoding='utf-8') as f:
    pos = [int(x) for x in f.read().rstrip().split(",")]
    
min_fuel = 1000000000
for n in range(min(pos),max(pos)):
    fuel = 0
    for p in pos:
        fuel += abs(p-n)
    if fuel < min_fuel:
        min_fuel = fuel
        
print(min_fuel)