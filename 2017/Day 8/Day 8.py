import re

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

regs = {}
pattern = r'([a-z]{1,3}) (inc|dec) (\-?\d{1,5}) if ([a-z]{1,3}) (<|<=|==|!=|>=|>) (\-?\d{1,5})'
part2 = 0

for l in lines:
    g = re.match(pattern, l)
    reg, dir, change, src, arg, value = g.groups()
    change = int(change)
    if reg not in regs: regs[reg] = 0
    if src not in regs: regs[src] = 0
    
    if eval('regs[src]' + arg + value):
        if dir == 'inc':
            regs[reg] += change
        elif dir == 'dec':
            regs[reg] -= change
            
    part2 = max(part2, regs[reg])
    
part1 = max(regs.values())

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))