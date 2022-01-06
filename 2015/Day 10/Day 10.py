from itertools import groupby

input = '1113122113'
iter1 = 40
iter2 = 50

for i in range(iter2):
    input = ''.join([str(len([True for _ in g])) + str(k) for k, g in groupby(input)])
    if i == iter1 - 1:
        part1 = len(input)
    
part2 = len(input)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))