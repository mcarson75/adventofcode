import numpy as np

input = np.array([[int(x) for x in l.strip().split()] for l in open("input.txt", 'r', encoding='utf-8').readlines()])
input2 = input.T.reshape(len(input), 3)

def is_triangle(t):
    if sum(t[:2]) > t[2] and sum(t[1:]) > t[0] and (t[0] + t[2]) > t[1]:
        return True
    return False

part1 = sum(map(is_triangle, input))
part2 = sum(map(is_triangle, input2))

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
