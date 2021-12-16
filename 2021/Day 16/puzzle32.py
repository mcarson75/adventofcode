from math import prod

for line in open("input.txt", 'r', encoding='utf-8'):
    hex = line.strip()

hex_to_bit = lambda c: bin(int(c, 16))[2:].zfill(4)    
#bit_to_dec = lambda i: int(''.join([str(x) for x in i]), 2)
bit_to_dec = lambda i: int(i, 2)

def read_num(data, n):
    data, out = read_bits(data, n)
    return data, bit_to_dec(out)

b = ''.join([hex_to_bit(c) for c in hex])

version = 0

def read_bits(b, n):
    out = b[:n]
    b = b[n:]
    return b, out

def parse_packet(data):
    global version
    data, v = read_num(data, 3)
    data, tid = read_num(data, 3)
    version += v
    if tid == 4:
        t = ''
        while True:
            data, cnt = read_bits(data, 1)
            data, _ = read_bits(data, 4)
            t += _
            if cnt == '0': break
        return (data, bit_to_dec(t))
    else:
        data, ltid = read_bits(data, 1)
        sub = []
        if ltid == '0':
            data, sub_length = read_num(data, 15)
            data, subpackets = read_bits(data, sub_length)
            while subpackets:
                subpackets, x = parse_packet(subpackets)
                sub.append(x)
        else:
            data, num_packets = read_num(data, 11)
            for i in range(num_packets):
                data, x = parse_packet(data)
                sub.append(x)
    if tid == 0:
        return (data, sum(sub))
    if tid == 1:
        return (data, prod(sub))
    if tid == 2:
        return (data, min(sub))
    if tid == 3:
        return (data, max(sub))
    if tid == 5:
        return (data, 1 if sub[0] > sub[1] else 0)
    if tid == 6:
        return (data, 1 if sub[0] < sub[1] else 0)
    if tid == 7:
        return (data, 1 if sub[0] == sub[1] else 0)
    
    return data

print(parse_packet(b)[1])