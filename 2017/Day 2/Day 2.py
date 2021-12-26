lines = [l.strip().split() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
total_diff = 0
total_divisor = 0
for l in lines:
    s = sorted([int(i) for i in l], reverse = True)
    total_diff += max(s) - min(s)
    while True:
        b = [s[0] % n for n in s[1:]]
        if 0 in b:
            total_divisor += s[0] // s[b.index(0) + 1]
            break
        else:
            s.pop(0)
                
print("Part 1: " + str(total_diff))
print("Part 2: " + str(total_divisor))