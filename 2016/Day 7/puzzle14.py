lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

check_string = lambda nib: nib[0] == nib[2] and nib[0] != nib[1]
reverse_nib = lambda nib: ''.join([nib[1], nib[0], nib[1]]) if check_string(nib) else ''

ssl = 0
for l in lines:
    nibs = [l[i:i+3] for i in range(0, len(l)-2)]
    ib = False
    nib_in = set()
    valid = set()
    for nib in nibs:
        if '[' in nib:
            ib = True
        elif ']' in nib:
            ib = False
        elif ib:
            nib_in.add(nib)
        elif not ib and check_string(nib):
            valid.add(nib)
    for nib in nib_in:
        if reverse_nib(nib) in valid:
            ssl += 1
            break
        
print(ssl)