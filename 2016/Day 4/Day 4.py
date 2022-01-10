import re
from collections import Counter

rooms = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

pattern = r'(?P<name>.+)-(?P<id>\d{1,4})\[(?P<checksum>[a-z]{5})\]'

def rotate(c, n):
    ans = ord(c) + n % 26
    if ans > ord('z'):
        ans = ans - ord('z') + ord('a') - 1
    return chr(ans)

part1 = 0
for r in rooms:
    room = re.match(pattern, r).groupdict()
    name = room['name']
    id = int(room['id'])
    name = name.replace('-', '')
    c = Counter(name)
    d = sorted(c.most_common(), key = lambda item: (-item[1], item[0]))
    check = ''.join([c[0] for c in d[:5]])
    if check == room['checksum']:
        part1 += id

    new = ''.join(rotate(c, id) for c in name)
    if 'north' in new:            
        part2 = id
                
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))