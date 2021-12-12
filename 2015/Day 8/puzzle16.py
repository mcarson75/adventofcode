with open("input.txt", 'r', encoding='utf-8') as f:
    score = sum([(2+line.count('\\') + line.count('"')) for line in f])
        
print(score)       
        