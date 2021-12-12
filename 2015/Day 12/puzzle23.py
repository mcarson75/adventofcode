import re

with open("input.txt", 'r', encoding='utf-8') as f:
    input = f.read()
    
num = [int(x) for x in re.findall(r'[-\d]+', input)]
    
print(sum(num))