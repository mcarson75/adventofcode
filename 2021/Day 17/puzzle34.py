# target area: x=32..65, y=-225..-177

def launch(vx, vy):
    min_x, max_x, min_y, max_y = [32, 65, -225, -177]
    x, y = [0, 0]
    m = 0
    while x <= max_x and y >= min_y:
        x += vx
        y += vy
        vx = max(0, vx -1)
        vy -= 1
        m = max(m, y)
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True, m
    return False, 0
    
target_set = set()
for vx in range(8, 66):
    for vy in range(-230, 300):
        target, height = launch(vx, vy)
        if target:
            target_set.add((vx, vy))
        
print(len(target_set))