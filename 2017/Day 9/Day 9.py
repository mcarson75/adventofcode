char = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

# Remove garbage
garbage = []
cur_state = False
ignore_next = False
toggle_next = False
part2 = 0

for n in range(len(char)):
    if not ignore_next:
        if toggle_next:
            cur_state = False
            toggle_next = False
        if char[n] == '!':
            ignore_next = True
        elif char[n] == '<' and not cur_state:
            cur_state = True
        elif char[n] == '>' and cur_state:
            toggle_next = True
        elif cur_state:
            part2 += 1
    else:
        ignore_next = False
        
    garbage.append(cur_state)

# Count groups
char = ''.join([char[n] for n in range(len(char)) if not garbage[n]])

part1 = 0
score = 1
for c in char:
    if c == '{':
        part1 += score
        score += 1
    elif c == '}':
        score -= 1

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))