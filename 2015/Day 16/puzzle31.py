import re

pattern = r"Sue (\d{1,3}): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)"

match = {"children" : 3,
         "cats" : 7,
         "samoyeds" : 2,
         "pomeranians" : 3,
         "akitas" : 0,
         "vizslas" : 0,
         "goldfish" : 5,
         "trees" : 3,
         "cars" : 2,
         "perfumes" : 1}

for line in open("input.txt", 'r', encoding='utf-8'):
    m = re.match(pattern, line.strip())
    num = int(m.group(1))
    if not match[m.group(2)] == int(m.group(3)):
        continue
    if not match[m.group(4)] == int(m.group(5)):
        continue
    if not match[m.group(6)] == int(m.group(7)):
        continue
    print(num)