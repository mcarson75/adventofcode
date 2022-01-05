from hashlib import md5

input = 'bgvyzdsv'

part1 = False
part2 = False
num = 0

while True:
    hash = md5(str.encode(input + str(num))).hexdigest()
    if not part1 and hash[0:5] == '00000':
        part1 = num
    if not part2 and hash[0:6] == '000000':
        part2 = num
    if part1 and part2:
        break
    num += 1

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
