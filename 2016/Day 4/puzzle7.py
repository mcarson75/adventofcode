import re

rooms = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

pattern = r'(.+)-(\d{1,4})\[([a-z]{5})\]'

id_total = 0
for r in rooms:
    groups = re.match(pattern, r)
    s = groups[1]
    s = s.replace('-', '')
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    d_sort = (sorted(d.items(), key = lambda item: (-item[1], item[0])))
    check = ''.join([c[0] for c in d_sort[:5]])
    if check == groups[3]:
        id_total += int(groups[2])
        
print(id_total)