text = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

def decompress(s):
    length = 0
    i = 0
    marker = False
    marker_text = ''
    while i < len(s):
        c = s[i]
        if not marker and c != '(':
            length += 1
        elif not marker and c == '(':
            marker = True
        elif marker and c == ')':
            lg, tm = map(int, marker_text.split('x'))
            t = s[i+1:i+lg+1]
            o = decompress(t)
            length += o * tm           
            i += lg
            marker = False
            marker_text = ''
        elif marker:
            marker_text += c
        i += 1
        
    return length
    
print(decompress(text))