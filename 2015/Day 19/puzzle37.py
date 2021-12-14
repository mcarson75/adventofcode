lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
input = lines[-1]
lines = [l.split(' => ') for l in lines[:-2]]

repl = {}
for l, r in lines:
    if l in repl:
        repl[l].append(r)
    else:
        repl[l] = [r]

new = set()

for left in repl.keys():
    for m in repl[left]:
        for s in range(len(input)):
            if input[s:s+len(left)] == left:
                new_string = input[:s] + m + input[s+len(left):]
                new.add(new_string)

print(len(new))