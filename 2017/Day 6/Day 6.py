banks = [int(x) for x in [l.strip().split() for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]]

count = 1
part1 = False
states = set()
states.add(tuple(banks))

while True:
    i = banks.index(max(banks))
    m = banks[i]
    banks[i] = 0
    j = i + 1 if i < len(banks) - 1 else 0
    for n in range(m):
        banks[j] += 1
        j += 1
        j = 0 if j > (len(banks) - 1) else j
    if part1 and tuple(banks) == s:
        part2 = count
        break
    if tuple(banks) in states:
        if not part1:
            part1 = count
            count = 0
            s = tuple(banks)
    else:
        states.add(tuple(banks))
    count += 1
    
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))