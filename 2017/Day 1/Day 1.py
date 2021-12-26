num = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

total = sum([int(num[i]) for i in range(len(num)-1) if num[i] == num[i + 1]])
total += int(num[0]) if num[0] == num[-1] else 0

print("Part 1: " + str(total))

step = len(num) // 2
total = 2* sum([int(num[i]) for i in range(step - 1) if num[i] == num[i + step]])

print("Part 2: " + str(total))