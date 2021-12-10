with open("input.txt", 'r', encoding='utf-8') as f:
    array = f.readlines()

def find_close(s):
    for i in range(len(s)):
        if s[i] in closing:
            return i
    return None

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
scores = [3, 57, 1197, 25137]
    
score = 0
for s in array:
    s = list(s)
    
    while True:
        i = find_close(s)
        if i is None:
            break
        nc = s[i]
        nc_index = closing.index(nc)
        if i > 0 and s[i-1] == opening[nc_index]:
            del s[i-1:i+1]
        else:
            score += scores[nc_index]
            break
        
print(score)          
    