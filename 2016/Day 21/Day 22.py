import numpy as np
import re

swap_pattern = r'swap (position|letter) (\S+) with (position|letter) (\S+)'
rotate_pattern = r'rotate (left|right) (\d+) steps?'
rotate_based_pattern = r'rotate based on position of letter (\S+)'
reverse_pos_pattern = r'reverse positions (\d+) through (\d+)'
move_pos_pattern = r'move position (\d+) to position (\d+)'

commands = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

def run_commands(commands, password, reversed = False):
    def get_index(c):
        return int(np.where(password == c)[0])

    password = np.array(list(password))

    if reversed: commands.reverse()
    
    for c in commands:
        if 'swap' in c:
            match = re.search(swap_pattern, c)
            if match[1] == 'position':
                x, y = int(match[2]), int(match[4])
            else:
                x, y = get_index(match[2]), get_index(match[4])
            password[[y, x]] = password[[x, y]]
        elif 'rotate based' in c:
            match = re.search(rotate_based_pattern, c)
            i = get_index(match[1])
            if not reversed:
                i += 2 if i >=4 else 1
            else:
                if i == 0:
                    i = -9
                elif i % 2 == 1:
                    i = -(i // 2 + 1)
                else:
                    i = -(i // 2 + 5)
            password = np.roll(password, i)
        elif 'rotate' in c:
            match = re.search(rotate_pattern, c)
            i = int(match[2])
            if match[1] == 'left': i = -i
            if reversed: i = -i
            password = np.roll(password, i)
        elif 'reverse' in c:
            match = re.search(reverse_pos_pattern, c)
            x, y = int(match[1]), int(match[2])
            password[x:y+1] = password[x:y+1][::-1]
        elif 'move' in c:
            match = re.search(move_pos_pattern, c)
            x, y = int(match[1]), int(match[2])
            i = -1 if x < y else 1
            if reversed: i = -i
            if x < y:
                password[x:y+1] = np.roll(password[x:y+1], i)
            else:
                password[y:x+1] = np.roll(password[y:x+1], i)
                
    return ''.join(password)

part1 = run_commands(commands, 'abcdefgh')
part2 = run_commands(commands, 'fbgdceah', reversed = True)  
      
print("Part 1: " + part1)
print("Part 2: " + part2)