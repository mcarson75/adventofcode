lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

check_string = lambda nib: nib[0] == nib[3] and nib[1] == nib[2] and nib[0] != nib[1]

tls = 0
for l in lines:
    nibs = [l[i:i+4] for i in range(0, len(l)-3)]
    ib = False
    valid = False
    for nib in nibs:
        if '[' in nib:
            ib = True
        if ']' in nib:
            ib = False
        if ib and check_string(nib):
            valid = False
            break
        if not ib and check_string(nib):
            valid = True
    if valid:
        tls += 1
        
print(tls)