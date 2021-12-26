import functools
from collections import defaultdict

Z = [1, 1, 1, 26, 1, 1, 26, 1, 26, 1, 26, 26, 26, 26]
X = [12, 13, 12, -13, 11, 15, -14, 12, -8, 14, -9, -11, -6, -5]
Y = [1, 9, 11, 6, 6, 13, 13, 5, 7, 2, 10, 14, 7, 1]

Zmax = [26**sum([z==26 for z in Z[i:]]) for i in range(len(Z))]

matrix = defaultdict()

@functools.lru_cache(maxsize=None)
def run(d, z, w):
    global matrix
    if (d, z, w) in matrix:
        return matrix[(d, z, w)]
    else:
        x = X[d] + (z % 26)
        z //= Z[d]
        if x != w:
            z *= 26
            z += w + Y[d]
        #matrix[(d, z, w)] = z
        return z

@functools.lru_cache(maxsize=None)
def search(digit, z):
    if digit == 14:
        return [''] if z==0 else []
    if z > Zmax[digit]: return []
    x = X[digit] + (z % 26)
    if x in range(1, 10):
        w_range = range(x, x + 1)
    else:
        w_range = range(1, 10)
    ret = []
    for w in w_range:
        zn = run(digit, z, w)
        if digit==13 and zn==0:
            print("stop")
        nxt = search(digit + 1, zn)
        for x in nxt:
            ret.append(str(w) + x)
    return ret
    
ans = search(0, 0)
ans = [int(x) for x in ans]
print(max(ans))