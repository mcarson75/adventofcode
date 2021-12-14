pairs = {}

for line in open("input.txt", 'r', encoding='utf-8'):
    if len(line.strip()) > 10:
        string = line.strip()
    elif '->' in line:
        p, r = line.strip().split(' -> ')
        pairs[p] = r

rep = 10

for n in range(rep):
    _add = [pairs[s] for s in [string[n:n+2] for n in range(len(string) -1)]]
    new_string = ''
    for n in range(len(string)-1):
        new_string += string[n] + _add[n]
    string = new_string + string[-1]
    
results = {}

for c in string:
    if c not in results:
        results[c] = 1
    else:
        results[c] += 1
        
print(max(results.values()) - min(results.values()))
        