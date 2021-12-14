lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
string = lines[0]
rules = {r[0]: r[1] for r in [l.split(' -> ') for l in lines[2:]]}

rep = 40

pairs = {}
_add = [string[n:n+2] for n in range(len(string)-1)]
for a in _add:
    if a not in pairs:
        pairs[a] = 1
    else:
        pairs[a] += 1

for n in range(rep):
    new_pairs = {}
    for couple, cnt in pairs.items():
        new = couple[0] + rules[couple] + couple[1]
        for c in [new[n:n+2] for n in range(2)]:
            if c in new_pairs:
                new_pairs[c] += cnt
            else:
                new_pairs[c] = cnt
    pairs = new_pairs

totals = {}
for couple, cnt in pairs.items():
    for n in range(2):
        if couple[n] in totals:
            totals[couple[n]] += cnt
        else:
            totals[couple[n]] = cnt
totals[string[0]] += 1
totals[string[-1]] += 1

count = [i//2 for i in totals.values()]
        
print(max(count) - min(count))
        