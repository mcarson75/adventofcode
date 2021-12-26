import functools

DZ = [1, 1, 1, 26, 1, 1, 26, 1, 26, 1, 26, 26, 26, 26]
AX = [12, 13, 12, -13, 11, 15, -14, 12, -8, 14, -9, -11, -6, -5]
AY = [1, 9, 11, 6, 6, 13, 13, 5, 7, 2, 10, 14, 7, 1]

Zmax = [26**len([x for x in range(len(DZ)) if DZ[x]==26 and x >= i]) for i in range(len(DZ))]

def run(ch, z, w):
    x = AX[ch] + (z % 26)
    z //= DZ[ch]
    if x != w:
        z *= 26
        z += w + AY[ch]
    return z

@functools.lru_cache(maxsize=None)
def search(ch, z):
    if ch == 14:
        return [''] if z==0 else []
    if z > Zmax[ch]: return []
    wopts = list(range(1,10))
    x = AX[ch] + (z % 26)
    if x in range(1, 10):
        wopts = [x]
    ret = []
    for w in wopts:
        zn = run(ch, z, w)
        nxt = search(ch + 1, zn)
        for x in nxt:
            ret.append(str(w) + x)
    return ret
    
ans = search(0, 0)
ans = [int(x) for x in ans]
print(min(ans))