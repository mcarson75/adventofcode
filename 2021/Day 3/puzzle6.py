column_bit = lambda matrix, i: int(sum([row[i] for row in matrix])/len(matrix) + 0.5)

def filter_bitwise(array, crit):
    pos = 0
    while len(array) > 1:
        s = column_bit(array, pos)
        array = [x for x in array if x[pos] == crit(s)]
        pos += 1

    return int(''.join(str(e) for e in array[0]),2)

with open('input.txt', 'r', encoding='utf-8') as read_file:
    array = [list(map(lambda x: int(x), l.rstrip())) for l in read_file]

oxygen = filter_bitwise(array, lambda x: x)
co2 = filter_bitwise(array, lambda x: 1-x)

print(oxygen * co2)
