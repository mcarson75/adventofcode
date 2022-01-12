with open("input.txt", 'r', encoding='utf-8') as f:
    commands = [l.strip().split() for l in f.readlines()]
    
regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def run_commands(regs):
    i = 0
    while True:
        if i >= len(commands):
            break
        
        if len(commands[i]) > 2:
            command, x, y = commands[i]
        else:
            command, y = commands[i]
        if command == 'cpy':
            regs[y] = int(x) if x.isnumeric() else regs[x]
        elif command == 'inc':
            regs[y] += 1
        elif command == 'dec':
            regs[y] -= 1
        elif command == 'jnz':
            check = int(x) if x.isnumeric() else regs[x]
            if check != 0:
                i += int(y) - 1
        i += 1

    return regs

part1 = run_commands(regs)['a']
regs['c'] = 1
part2 = run_commands(regs)['a']

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))