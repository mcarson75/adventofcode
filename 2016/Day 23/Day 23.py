with open("input.txt", 'r', encoding='utf-8') as f:
    commands = [l.strip().split() for l in f.readlines()]

# pseudocode simplifies to a! + (cpy parameter in line 20) * (jnz parameter in line 21)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    
    return fact
    
_, mult1, _ = commands[19]
_, mult2, _ = commands[20]

mult = int(mult1) * int(mult2)

part1 = factorial(7) + mult
part2 = factorial(12) + mult

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))