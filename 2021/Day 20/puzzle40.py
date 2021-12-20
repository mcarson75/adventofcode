import numpy as np

def decode(input, code, default = '.'):
    input = np.concatenate((np.full((len(input),1), default), input, np.full((len(input),1), default)),1)

    input = np.concatenate((np.full((1,len(input[0])), default), input, np.full((1, len(input[0])), default)),0)

    out = np.full_like(input, '.')

    input = np.concatenate((np.full((len(input),1), default), input, np.full((len(input),1), default)),1)
    input = np.concatenate((np.full((1,len(input[0])), default), input, np.full((1, len(input[0])), default)),0)

    for i in range(len(out)):
        for j in range(len(out[0])):
            x, y = j+1, i+1
            sub = input[y-1:y+2, x-1:x+2]
            sub = np.reshape(sub, (1, 9))[0]
            check = ''.join(['0' if s=='.' else '1' for s in sub ])
            out[i][j] = code[int(check,2)]
            
    return out

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f.readlines()]
    
code = list(lines[0])
input = np.array([list(l) for l in lines[2:]])

reps = 50
for n in range(reps):
    if n % 2 != 0: 
        default = '#'
    else:
        default = '.'
    input = decode(input, code, default)
    
num = np.count_nonzero(input=='#')
print(num)