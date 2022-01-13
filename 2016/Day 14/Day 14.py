from hashlib import md5

input = 'yjdafjpo'

def check_repeat(hash, size):
    nibs = [hash[i:i+size] for i in range(len(hash)-size + 1)]
    for n in nibs:
        if all([c==n[0] for c in n]):
            return n[0]
    return None

def find_hash(stretch = False):
    num = 0
    pending = set()
    valid = []

    while len(valid) < 64:
        pending = {p for p in pending if p[0] > num - 1000}

        hash = md5(str.encode(input + str(num))).hexdigest()
        if stretch:
            for n in range(2016):
                hash = md5(str.encode(hash)).hexdigest()
                
        ck_3 = check_repeat(hash, 3)
        ck_5 = check_repeat(hash, 5)

        if ck_5:
            new_keys = {p for p in pending if p[1]==ck_5 and p[0] != num}
            pending.difference_update(new_keys)
            valid.extend([p[0] for p in new_keys])

        if ck_3:
            pending.add((num, ck_3))
                
        num += 1
        
    valid.sort()
    return valid[63]

part1 = find_hash()
part2 = find_hash(True)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))