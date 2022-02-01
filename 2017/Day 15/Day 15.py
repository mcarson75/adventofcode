from collections import deque

genA = 618
genB = 814

def next_gen(prev, factor): return prev * factor % 2147483647
def right_match(a, b): return a & 0xFFFF == b & 0xFFFF

part1 = 0
part2 = 0
reps1 = 40000000
reps2 = 5000000
iter = 0
Aq = deque()
Bq = deque()
for _ in range(reps1):
    genA = next_gen(genA, 16807)
    genB = next_gen(genB, 48271)
    if right_match(genA, genB):
        part1 += 1
    if iter < reps2:
        if genA % 4 == 0:
            Aq.append(genA)
        if genB % 8 == 0:
            Bq.append(genB)
        for _ in range(min(len(Aq), len(Bq))):
            iter += 1
            A = Aq.popleft()
            B = Bq.popleft()
            if right_match(A, B):
                part2 += 1
    
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))