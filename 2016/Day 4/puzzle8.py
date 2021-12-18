import re

rooms = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

pattern = r'(.+)-(\d{1,4})\[([a-z]{5})\]'

def rotate(c, n):
    ans = ord(c) + n % 26
    # the below if-statement makes sure the value does not overflow.
    if ans > ord('z'):
        ans = ans - ord('z') + ord('a') - 1
    return chr(ans)

for r in rooms:
    groups = re.match(pattern, r)
    s = groups[1]
    s = s.replace('-', ' ')
    id = int(groups[2])
    new = ''
    for c in s:
        if c != ' ':
            new += rotate(c, id)
        else:
            new += ' '
    if 'north' in new:            
        print(new + ' ' + str(id))