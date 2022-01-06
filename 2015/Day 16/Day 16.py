import re

pattern = r"Sue (\d{1,3}): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)"

match = {"children" : 3,
         "cats" : 7,
         "samoyeds" : 2,
         "pomeranians" : 3,
         "akitas" : 0,
         "vizslas" : 0,
         "goldfish" : 5,
         "trees" : 3,
         "cars" : 2,
         "perfumes" : 1}

for line in open("input.txt", 'r', encoding='utf-8'):
    m = re.match(pattern, line.strip())
    num = int(m.group(1))
    keys = [m.group(n) for n in range(2,7,2)]
    values = [int(m.group(n)) for n in range(3,8,2)]
    props = {k: v for k, v in zip(keys, values)}

    if all([props[k] == match[k] for k in keys]):
        part1 = num
        
    valid = True
    for p in props.keys():
        if p == 'cats' or p == 'trees':
            if props[p] <= match[p]: valid = False
        elif p == 'pomeranians' or p == 'goldfish':
            if props[p] >= match[p]: valid = False
        else:
            if props[p] != match[p]: valid = False
    
    if valid: part2 = num
    
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))