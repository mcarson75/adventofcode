lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
input = lines[-1]
lines = [l.split(' => ') for l in lines[:-2]]
part2 = 0

def replace_n(search, repl, txt, n):
    arr = txt.split(search)
    if len(arr) == 1 or len(arr) <= n:
        return False
    left = search.join(arr[:n])
    right = search.join(arr[n:])
    
    return left + repl + right

def finished(s): return all([c=='e' for c in s])

part1 = set()
for left, right in lines:
    for n in range(input.count(left)):
        part1.add(replace_n(left, right, input, n + 1))

while not finished(input):
    for left, right in lines:
        new_input = replace_n(right, left, input, -1)
        if new_input:
            part2 += 1
            input = new_input

print("Part 1: " + str(len(part1)))
print("Part 2: " + str(part2))