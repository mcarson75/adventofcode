import numpy as np

operator = {'AND': '&', 'OR': '|', 'LSHIFT': '<<', 'RSHIFT': '>>', 'NOT': '~'}

def get_value(i):
    if i.isnumeric():
        return int(i)
    else:
        return outputs[i]

def run_commands(outputs):
    n = 0
    while not outputs['a']:
        c = commands[n]
        input = c[0]
        output = c[1]
        if not outputs[output]:
            if 'AND' in input or 'OR' in input or 'LSHIFT' in input or 'RSHIFT' in input:
                i1, c, i2 = input.split()
                i1, i2 = get_value(i1), get_value(i2)
                if i1 != None and i2 != None:
                    outputs[output] = eval('i1' + operator[c] + 'i2')
            elif 'NOT' in input:
                i1 = get_value(input.split(' ')[1])
                if i1 != None:
                    outputs[output] = ~i1    
                    if outputs[output] < 0:
                        outputs[output] += 65536    
            else:
                outputs[output] = get_value(input)
        
        
        n += 1
        if n >= len(commands):
            n = 0
            
    return outputs['a']

with open("input.txt", 'r', encoding='utf-8') as f:
    commands = np.array([s.strip().split(' -> ') for s in f.readlines()])

outputs = {key: None for key in list(commands[:, 1])}
part1 = run_commands(outputs)

outputs = {key: None for key in list(commands[:, 1])}
outputs['b'] = part1

part2 = run_commands(outputs)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))