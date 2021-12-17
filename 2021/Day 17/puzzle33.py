# target area: x=32..65, y=-225..-177

from math import floor, ceil

target = [32, 65, -225, -177]
n = abs(target[2])

highest = int(n * (n-1) /2)

def check_x(x):
    return (1 + (1 + 8*x)**0.5) / 2
    
if floor(check_x(target[1])) >= ceil(check_x(target[0])):
    print(highest)
else:
    print("Not possible")