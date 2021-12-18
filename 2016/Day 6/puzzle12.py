from collections import Counter

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

letters = [[l[i] for l in lines] for i in range(len(lines[0]))]

ans = ''
for l in letters:
    ans += Counter(l).most_common()[-1][0]

print(ans)