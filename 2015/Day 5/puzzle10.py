with open("input.txt", 'r', encoding='utf-8') as f:
    strings = [s.rstrip() for s in f.readlines()]

num = 0

indices = list(range(len(strings[0])))

for s in strings:
    if len([True for x, y in zip(s[2:], s[:-2]) if x==y]) > 0:
        for n in range(len(s)-1):
            i = [s for s in range(n, n+2)]
            source = "".join([s[b] for b in i])
            if len(s.split(source)) > 2:
                num += 1
                break
        
print(num)