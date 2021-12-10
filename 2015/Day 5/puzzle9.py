with open("input.txt", 'r', encoding='utf-8') as f:
    strings = [s.rstrip() for s in f.readlines()]

num = 0
bad = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']

for s in strings:
    if any([i in s for i in bad]):
        continue
    if sum([i in vowels for i in s]) >=3 and len([True for x, y in zip(s[1:], s[:-1]) if x==y]) >0:
        num += 1
        
print(num)
