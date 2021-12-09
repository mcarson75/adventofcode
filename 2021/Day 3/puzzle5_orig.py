def calc_decimal(binary):
    exp=0
    dec=0
    
    for i in range(len(binary)-1, -1, -1):
        dec += (binary[i] * (2**exp))
        exp += 1

    return dec

def get_gamma_epsilon(filename):
    from numpy import add

    array = []
    with open(filename, 'r', encoding='utf-8') as read_file:
        lines=read_file.read().splitlines()
        
    for line in lines:
        line_array=[]
        for i, v in enumerate(line):
            line_array.append(int(v))
        array.append(line_array)

    sum_array = [0]*len(array[0])
    for line in array:
        sum_array = add(sum_array, line)

    gamma = []
    epsilon = []
    for s in sum_array:
        if s > (len(array)/2):
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)

    return calc_decimal(gamma) * calc_decimal(epsilon)

print(get_gamma_epsilon('input.txt'))
