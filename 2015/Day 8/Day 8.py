
lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
    
part1 = sum([(len(l) - len(eval(l))) for l in lines])
part2 = sum([(2 + l.count('\\') + l.count('"')) for l in lines])
        
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
