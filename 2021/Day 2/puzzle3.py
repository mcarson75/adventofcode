def get_new_position(filename):
    from numpy import prod
    
    position = [0, 0]

    with open(filename, 'r', encoding='utf-8') as read_file:
        for line in read_file:
            dir, num = line.split()[0], int(line.split()[1])
            if dir=='forward':
                position[0] += num
            elif dir=='down':
                position[1] += num
            elif dir=='up':
                position[1] -= num
    
    return prod(position)

print(get_new_position('input.txt'))
