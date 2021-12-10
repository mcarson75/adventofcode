import numpy as np

def get_value(i):
    if i.isnumeric():
        return int(i)
    else:
        return outputs[i]

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [s.rstrip() for s in f.readlines()]

commands = []
    
for l in lines:
    commands.append(l.split(' -> '))
    
commands = np.array(commands)

outputs = {key: None for key in list(commands[:, 1])}

n = 0
while not outputs['a']:
    c = commands[n]
    input = c[0]
    output = c[1]
    if not outputs[output]:
        if 'AND' in input:
            [i1, i2] = [get_value(i) for i in input.split(' AND ')]
            if i1 != None and i2 != None:
                outputs[output] = i1 & i2        
        elif 'OR' in input:
            [i1, i2] = [get_value(i) for i in input.split(' OR ')]
            if i1 != None and i2 != None:
                outputs[output] = i1 | i2        
        elif 'LSHIFT' in input:
            [i1, i2] = [get_value(i) for i in input.split(' LSHIFT ')]
            if i1 != None and i2 != None:
                outputs[output] = i1 << i2        
        elif 'RSHIFT' in input:
            [i1, i2] = [get_value(i) for i in input.split(' RSHIFT ')]
            if i1 != None and i2 != None:
                outputs[output] = i1 >> i2        
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
        
print(outputs['a'])