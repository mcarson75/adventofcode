with open("input.txt", 'r', encoding='utf-8') as f:
    score = sum([(len(line.rstrip()) - len(eval(line))) for line in f])
        
print(score)       
        