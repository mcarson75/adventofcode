for line in open("input.txt", 'r', encoding='utf-8'):
    hex = line.strip()

hex_to_bit = lambda c: bin(int(c, 16))[2:].zfill(4)    
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
            if cnt == '0': break
    else:
        data, ltid = read_bits(data, 1)
        if ltid == '0':
            data, sub_length = read_num(data, 15)
            data, subpackets = read_bits(data, sub_length)
            while subpackets:
                subpackets = parse_packet(subpackets)
        else:
            data, num_packets = read_num(data, 11)
            for i in range(num_packets):
                data = parse_packet(data)
    return data
        
parse_packet(b)        

print(version)