with open("input.txt", 'r', encoding='utf-8') as f:
    strings = [s.rstrip() for s in f.readlines()]

part1 = 0
part2 = 0
bad = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']

for s in strings:
    if not any([i in s for i in bad]) and sum([i in vowels for i in s]) >= 3 and len([True for x, y in zip(s[1:], s[:-1]) if x==y]) > 0:
        part1 += 1
    if len([True for x, y in zip(s[2:], s[:-2]) if x==y]) > 0:
        two = [''.join(s[n:n+2]) for n in range(len(s) - 1)]
        if any([len(s.split(i)) > 2 for i in two]):
            part2 += 1
        
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
