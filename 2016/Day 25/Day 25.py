with open("input.txt", 'r', encoding='utf-8') as f:
    commands = [l.strip().split() for l in f.readlines()]
    
# pseudocode simplifies to 
# d = a + (parameter of cpy in line 2) * (parameter of cpy in line 3)
# while true {
#   a = d
#   while a != 0 {
#     b = a % 2
#     a /= 2
#     output b
#   }
# }
#
# This means we need to find the smallest number a such that binary representation of d = a + mult is '10' repeated in some form

_, mult1, _ = commands[1]
_, mult2, _ = commands[2]

mult = int(mult1) * int(mult2)

bin_len = len(bin(mult)) - 2
if bin_len % 2 == 1:
    bin_len += 1

part1 = 0

while part1 <= 0:    
    bin_num = int('10' * (bin_len // 2), 2)
    part1 = bin_num - mult
    bin_len += 2

print("Part 1: ", part1)