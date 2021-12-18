from math import ceil
from itertools import permutations

lines = []
for line in open("input.txt", 'r', encoding='utf-8'):
    lines.append(eval(line.strip()))

def add_end(x, n, side):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    if side == 'left':
        return [add_end(x[0], n, 'left'), x[1]]
    elif side == 'right':
        return [x[0], add_end(x[1], n, 'right')]

def explode(x, n):
    #return is 1) if exploded 2) new left 3) new middle 4) new right
    if isinstance(x, int):
        return False, None, x, None
    if n==0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, left, a, right = explode(a, n-1)
    if exp:
       return True, left, [a, add_end(b, right, 'left')], None
    exp, left, b, right = explode(b, n-1)
    if exp:
       return True, None, [add_end(a, left, 'right'), b], right
    return False, None, x, None

def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x //2, ceil(x / 2)]
        return False, x
    a, b = x
    mod, a = split(a)
    if mod: return True, [a, b]
    mod, b = split(b)
    return mod, [a, b]

def add(a, b):
    x = [a, b]
    while True:
        mod, _, x, _ = explode(x, 4)
        if mod: continue
        mod, x, = split(x)
        if not mod: break
    return x

def magnitude(x):
    if isinstance(x, int): return x
    return 3 * magnitude(x[0]) + 2* magnitude(x[1])

ans = max(magnitude(add(a, b)) for a, b in permutations(lines, 2))

print(ans)    