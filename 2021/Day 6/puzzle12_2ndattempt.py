import sys
sys.setrecursionlimit(10000)
import numpy as np

days = 80

fish_per_day=[]
for d in range(1, days+1):
    array=np.array([(d+8)+7*f for f in range(0,int((days-8-d)/7))])
    fish_per_day.append(array)
    print(array)

def count_fish(start, interval):
    new_fish = [start + interval * d for d in range(0,int((days-start)/interval)+1)]
    #print(new_fish)

    added_fish = len(new_fish)
    print(added_fish)

    for d in new_fish:
        #added_fish += count_fish(d, 9)
        print([d + 9 * e for e in range(0,int((days-d)/9)+1)])
        #print(added_fish)

    return added_fish

with open('input.txt', 'r', encoding='utf-8') as read_file:
    lines = read_file.readlines()

fish = lines[0].rstrip().split(",")
fish = [int(f,10) for f in fish]

total_fish = 0

#for n in range(1,6):
    #print(count_fish(n,7))
    #total_fish += count_fish(n, 7) * fish.count(n)

print(total_fish)
