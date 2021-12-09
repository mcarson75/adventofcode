with open("input.txt", 'r', encoding='utf-8') as f:
    pos = [int(x) for x in f.read().rstrip().split(",")]
 
min_fuel = None
avg = int(sum(pos)/len(pos))
for n in range(avg,(avg)+2):
    fuel = 0
    for p in pos:
        fuel += abs(p-n)*(abs(p-n)+1)/2
    if not min_fuel or fuel < min_fuel:
        min_fuel = int(fuel)
        
print(min_fuel)