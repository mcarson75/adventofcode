with open("input.txt", 'r', encoding='utf-8') as f:
    pos = [int(x) for x in f.read().rstrip().split(",")]
 
min_fuel = None   
for n in range(min(pos),max(pos)):
    fuel = 0
    for p in pos:
        fuel += sum(range(abs(p-n)+1))
    if not min_fuel or fuel < min_fuel:
        min_fuel = fuel
        
print(min_fuel)