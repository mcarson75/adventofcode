text = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

output = ''
i = 0
marker = False
marker_text = ''
while i < len(text):
    c = text[i]
    if not marker and c != '(':
        output += c
    elif not marker and c == '(':
        marker = True
    elif marker and c == ')':
        lg, tm = map(int, marker_text.split('x'))
        t = text[i+1:i+lg+1]
        for n in range(tm):
            output += t
        i += lg
        marker = False
        marker_text = ''
    elif marker:
        marker_text += c
    i += 1 
    
print(len(output))      