import re

pattern = r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)\.'

txt = open("input.txt", 'r', encoding='utf-8').read()
discs = [list(map(int,t)) for t in re.findall(pattern, txt)]

def check_disc(d, t):
    return (d[0] + d[2] + t) % d[1] == 0
  
def get_time(discs):
    time = 0
    
    while True:
        time += 1
        check = [check_disc(d, time) for d in discs]
        if all(check):
            break

    return time

part1 = get_time(discs)
discs.append([7, 11, 0])
part2 = get_time(discs)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
