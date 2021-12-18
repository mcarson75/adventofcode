from hashlib import md5

input = 'wtnhxymk'

pw = ''
num = 0
while len(pw) < 8:
    m = md5(str.encode(input + str(num))).hexdigest()
    if m[:5] == '00000':
        pw += m[5]
    num += 1
    
print(pw)