input = '1113122113'
iter = 40

def parse_string(s):
    out = ''
    count = 0
    pc = None
    for c in s:
        if pc and c != pc:
            out += str(count) + pc
            count = 1
            pc = c
        elif pc is None:
            pc = c
            count +=1
        else:
            count +=1

    out += str(count) + pc
            
    return out
            

for i in range(iter):
    input = parse_string(input)
    
print(len(input))
