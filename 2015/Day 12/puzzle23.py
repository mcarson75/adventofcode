import re
import json

def hook(obj):
    if "red" in obj.values(): return{}
    else: return obj

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = f.read()

input = str(json.loads(lines, object_hook=hook))

num = [int(x) for x in re.findall(r'[-\d]+', input)]
    
print(sum(num))