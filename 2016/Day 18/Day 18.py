row = ['^.'.find(c) for c in [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]]

def get_safe(input, reps):
    total = sum(input)
    
    for n in range(1, reps):
        input = [1] + input + [1]
        input = [1 if left == right else 0 for left, right in zip(input, input[2:])]
        total += sum(input)

    return total

part1 = get_safe(row, 40)
part2 = get_safe(row, 400000)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
