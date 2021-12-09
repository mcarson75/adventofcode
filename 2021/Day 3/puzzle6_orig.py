from numpy import add

def calc_decimal(binary):
    exp=0
    dec=0
    
    for i in range(len(binary)-1, -1, -1):
        dec += (binary[i] * (2**exp))
        exp += 1

    return dec

def find_most_common(array):
    sum_array = [0]*len(array[0])
    for line in array:
        sum_array = add(sum_array, line)

    out = []
    for s in sum_array:
        if s == (len(array)/2) or s == 0:
            out.append(1)
        elif s > (len(array)/2):
            out.append(1)
        else:
            out.append(0)

    return out

def opposite(array):
    out = []
    for l in array:
        if l:
            out.append(0)
        else:
            out.append(1)

    return out

def get_oxygen_co2(filename):

    array = []
    with open(filename, 'r', encoding='utf-8') as read_file:
        lines=read_file.read().splitlines()
        
    for line in lines:
        line_array=[]
        for i, v in enumerate(line):
            line_array.append(int(v))
        array.append(line_array)

    oxygen_array = array.copy()
    pos = 0
    while len(oxygen_array) > 1:
        remove_array = []
        search_array = find_most_common(oxygen_array)
        search = search_array[pos]
        for line in oxygen_array:
            if not line[pos] == search:
                remove_array.append(line)
        oxygen_array = [e for e in oxygen_array if e not in remove_array]
        pos += 1

    co2_array = array.copy()
    pos = 0
    while len(co2_array) > 1:
        remove_array = []
        search_array = find_most_common(co2_array)
        search = search_array[pos]
        for line in co2_array:
            if line[pos] == search:
                remove_array.append(line)
        co2_array = [e for e in co2_array if e not in remove_array]
        pos += 1

    print(oxygen_array)
    print(co2_array)
    return calc_decimal(oxygen_array[0]) * calc_decimal(co2_array[0])

print(get_oxygen_co2('input.txt'))
