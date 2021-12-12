#import numpy as np

iter = 10000
flash = 0

with open("input.txt", 'r', encoding='utf-8') as f:
    octo = [[int(x) for x in y.strip()] for y in f]

def increase_energy(x,y):
    global flash
    global flash_this_step
    
    octo[x][y] += 1
    if octo[x][y] == 10:
        l = [x,y]
        flash_this_step.append(l) if l not in flash_this_step else flash_this_step
        x_mod = range(max(x-1, 0), min(x+2, len(octo[0])))
        y_mod = range(max(y-1, 0), min(y+2, len(octo)))
        for i in x_mod:
            for j in y_mod:
                if not [i, j] == [x, y]:
                    increase_energy(i, j)                      

for n in range(iter):
    flash_this_step = []
    for x in range(len(octo[0])):
        for y in range(len(octo)):
            increase_energy(x, y)
    flash += len(flash_this_step)
    if len(flash_this_step) == 100:
        print(n + 1)
        break
    for x, y in flash_this_step:
        octo[x][y] = 0 
    
#print(flash)