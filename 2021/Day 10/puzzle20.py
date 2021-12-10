with open("input.txt", 'r', encoding='utf-8') as f:
    array = f.readlines()

def find_close(s):
    for i in range(len(s)):
        if s[i] in closing:
            return i
    return None

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
    
scores = []
for s in array:
    s = list(s.rstrip())
    score = 0
    
    while True:
        i = find_close(s)
        if i is None:
            for c in reversed(s):
                score = 5*score + (opening.index(c)+1)
            scores.append(score)
            break
        nc = s[i]
        nc_index = closing.index(nc)
        if i > 0 and s[i-1] == opening[nc_index]:
            del s[i-1:i+1]
        else:
            break

scores.sort()
index = int((len(scores)-1)/2)
        
print(scores[index])          
    