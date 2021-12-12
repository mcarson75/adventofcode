import re

with open("input.txt", 'r', encoding='utf-8') as f:
    input = f.read()
    
total = sum([int(x) for x in re.findall(r'[-\d]+', input)])
reds = [x for x in re.findall(r'{[^{]*?:\"red\".+?}', input)]
reds = ''.join(reds)
red_total = sum([int(x) for x in re.findall(r'[-\d]+', reds)])
    
print(total-red_total)