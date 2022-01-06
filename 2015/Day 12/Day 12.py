import re
import json

def hook(obj):
    if "red" in obj.values(): return{}
    else: return obj

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = f.read()

json_all = str(json.loads(lines))
json_nored = str(json.loads(lines, object_hook=hook))

part1 = sum([int(x) for x in re.findall(r'[-\d]+', json_all)])
part2 = sum([int(x) for x in re.findall(r'[-\d]+', json_nored)])
    
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
