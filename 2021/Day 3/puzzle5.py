from numpy import transpose

with open('input.txt', 'r', encoding='utf-8') as read_file:
    array = [list(map(lambda x: int(x),l.rstrip())) for l in read_file]
    
gamma = transpose(list(map(lambda x: round(sum(x)/len(x)), transpose(array))))
epsilon = list(map(lambda x: -x+1, gamma))

bin_to_dec = lambda y: sum([2**(len(y)-i-1)*x for i,x in enumerate(y)])

print(bin_to_dec(gamma) * bin_to_dec(epsilon))
