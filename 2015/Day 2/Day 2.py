paper  = lambda w, h, l: (2*w*h) + (2*h*l) + (2*w*l) + min(w*h, h*l, w*l)
ribbon = lambda w, h, l: (w*h*l) + min(2*(w+h), 2*(h+l), 2*(w+l))

total_paper = 0
total_ribbon = 0

with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        [w, h, l] = [int(x) for x in line.rstrip().split('x')]
        total_paper  += paper(w, h, l)
        total_ribbon += ribbon(w, h, l)
    
print("Part 1: " + str(total_paper))
print("Part 2: " + str(total_ribbon))