def factors(n):
    f = [int(i) for i in range(1, int(n**0.5) + 1) if n % i == 0]
    f.extend([int(n / d) for d in f if n != d*d])

    return sum(f), sum(d for d in f if n / d <= 50)

N = 36000000

n = 1
part1 = None
part2 = None

while True:
    a, b = factors(n)
    if not part1 and N < 10 * a:
        part1 = n
    if not part2 and N < 11 * b:
        part2 = n
    if part1 and part2:
        break
    n += 1
    
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))