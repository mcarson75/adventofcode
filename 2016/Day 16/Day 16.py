input = '10010000000110000'
input = [bool(int(i)) for i in list(input)]

des_length = 35651584

def expand(a):
    b = [not i for i in reversed(a)]
    a.append(False)
    a.extend(b)
    
    return a

def checksum(a):
    return [not a[i] ^ a[i+1] for i in range(0, len(a), 2)]

def get_checksum(i, length):
    while len(i) < length:
        i = expand(input)
        
    i = i[:length]

    cksum = i
    while len(cksum) % 2 == 0:
        cksum = checksum(cksum)

    return ''.join(['1' if c else '0' for c in cksum])

part1 = get_checksum(input.copy(), 272)
part2 = get_checksum(input.copy(), 35651584)

print("Part 1: " + part1)
print("Part 2: " + part2)
