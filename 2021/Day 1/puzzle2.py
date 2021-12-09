def get_increasing_ma_depth(filename):
    from numpy import diff

    with open(filename, 'r', encoding='utf-8') as read_file:
        depths = [int(x) for x in read_file]
	
    return sum(i>0 for i in diff([sum(depths[j:j+3]) for j in range(0,len(depths)-2)]))

print(get_increasing_ma_depth('depths.txt'))
