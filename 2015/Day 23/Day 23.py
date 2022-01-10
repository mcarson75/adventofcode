regs1 = {'a': 0, 'b': 0}
regs2 = {'a': 1, 'b': 0}

inst = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

def run_code(regs):
    n = 0

    while n < len(inst):
        
        i = inst[n][:3]
        j = inst[n][4:]
        
        inc = 1
        if i == 'hlf':
            regs[j] //= 2
        elif i == 'tpl':
            regs[j] *= 3
        elif i == 'inc':
            regs[j] += 1
        elif i == 'jmp':
            inc = int(j)
        elif i == 'jie':
            reg, offset = j.split(',')
            if regs[reg] % 2 == 0:
                inc = int(offset)
        elif i == 'jio':
            reg, offset = j.split(',')
            if regs[reg] == 1:
                inc = int(offset)

        n += inc
        
    return regs

part1 = run_code(regs1)
part2 = run_code(regs2)

print("Part 1: " + str(part1['b']))
print("Part 2: " + str(part2['b']))