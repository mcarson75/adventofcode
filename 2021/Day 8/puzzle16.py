alpha = lambda s: "".join(sorted(s))
contains = lambda a, b: all([_ in max([a,b], key=len) for _ in min([a,b], key=len)])
find_parent = lambda array, x: [s for s in array if contains(s, x)][0]
digit_total = 0

with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        [i,o] = line.rstrip().split("|")
        left = [alpha(s) for s in i.rstrip().split(" ")]
        right = [alpha(s) for s in o.lstrip().split(" ")]
        
        _1, _7, _4, *unknown, _8 = sorted(left, key=len)
        
        s5 = [s for s in unknown if len(s)==5]
        s6 = [s for s in unknown if len(s)==6]

        _9 = find_parent(s6, _4)
        s6.remove(_9)
        
        _3 = find_parent(s5, _1)
        s5.remove(_3)
        
        _5 = find_parent(s5, _9)
        s5.remove(_5)
        
        _6 = find_parent(s6, _5)
        s6.remove(_6)
        
        _2 = s5[0]
        _0 = s6[0]
        
        dig = [_0, _1, _2, _3, _4, _5, _6, _7, _8, _9]    
        
        dig_str = ''    
        for r in right:
            dig_str += str(dig.index(r))
            
        digit_total += int(dig_str)
    
print(digit_total)