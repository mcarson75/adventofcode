def factors(n):
    f = [int(i) for i in range(1, int(n**0.5) + 1) if n % i ==0]
    f.extend([int(n / d) for d in f if n != d*d])
    f.sort()
    return sum(f[-50:])

N = 36000000

n=1
while N > 11 * factors(n): 
    n += 1
    
print(n)