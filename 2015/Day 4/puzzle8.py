from hashlib import md5

input = 'bgvyzdsv'

num = 0
while md5(str.encode(input + str(num))).hexdigest()[0:6] != '000000':
    num += 1
    
print(num)