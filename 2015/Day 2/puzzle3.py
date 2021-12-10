paper = lambda w, h, l: (2*w*h) + (2*h*l) + (2*w*l) + min(w*h, h*l, w*l)

total_paper = 0

with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        [w, h, l] = [int(x) for x in line.rstrip().split('x')]
        total_paper += paper(w, h, l)
    
print(total_paper)