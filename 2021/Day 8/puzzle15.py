num_1478=0

with open("input.txt", 'r', encoding='utf-8') as f:
    for l in f:
        [i,o] = l.rstrip().split("|")
        out = o.lstrip().split(" ")
        num_1478 += len([s for s in out if len(s) in [2, 3, 4, 7]])
        
    print(num_1478)