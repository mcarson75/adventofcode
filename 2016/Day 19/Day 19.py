input = 3014387
binary = "{:b}".format(int(input))
part1 = int(binary[1:] + binary[0], 2)

i = 1
while i * 3 < input:
    i *= 3

part2 = input - i

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))