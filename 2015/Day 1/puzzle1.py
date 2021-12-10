with open("input.txt", 'r', encoding='utf-8') as f:
    text = f.read()
    floors = text.count('(') - text.count(')')
    
print(floors)