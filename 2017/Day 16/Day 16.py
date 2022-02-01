import numpy as np

moves = [l.strip().split(',') for l in open("input.txt", 'r', encoding='utf-8').readlines()][0]

array = np.array(list('abcdefghijklmnop'))

def do_moves(array, reps):
    array_store = [''.join(array)]
    
    while True:
        for move in moves:
            if move[0] == 's':
                rot = int(move[1:])
                array = np.roll(array, rot)
            elif move[0] == 'x':
                i, j = [int(x) for x in move[1:].split('/')]
                array[i], array[j] = array[j], array[i]
            elif move[0] == 'p':
                x, y = move[1:].split('/')
                i = np.where(array == x)
                j = np.where(array == y)
                array[i], array[j] = array[j], array[i]
        
        array_str = ''.join(array)            
        if len(array_store) >= reps:
            return array_str
        elif not array_str in array_store:
            array_store.append(array_str)
        elif array_str in array_store:
            break

    index = reps % len(array_store)
    return array_store[index]

part1 = do_moves(array, 1)
array = np.array(list('abcdefghijklmnop'))
part2 = do_moves(array, 1000000000)
        
print("Part 1: " + part1)
print("Part 2: " + part2)