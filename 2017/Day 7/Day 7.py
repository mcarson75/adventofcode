progs = {}

class prog:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = set()
        self._weight = None
        
    def __repr__(self):
        return self.name
        
    @property
    def weight(self):
        return self._weight
        
    @weight.setter
    def weight(self, value):
        self._weight = int(value.replace('(','').replace(')',''))
        
    @property
    def tower_weight(self):
        return self.weight + sum([c.tower_weight for c in self.children])
    
    @property
    def child_weights(self):
        return [c.tower_weight for c in self.children]
    
    @property
    def balanced(self):
        if len(self.child_weights) > 0 and all(w == self.child_weights[0] for w in self.child_weights):
            return True
        if len(self.child_weights) == 0:
            return True
        return False
    
    @property
    def unbalanced(self):
        return not self.balanced and all([c.balanced for c in self.children])
    
    @property
    def unbalanced_child(self):
        if not self.unbalanced:
            return 0
        else:
            mcw = max(set(self.child_weights), key = self.child_weights.count)
            ub_child = [ch for ch in self.children if ch.tower_weight != mcw][0]
            return ub_child.weight + (mcw - ub_child.tower_weight)
    
lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

for l in lines:
    p, *c = l.split(' -> ')
    name, weight = p.split()
    if not name in progs:
        progs[name] = prog(name)
    progs[name].weight = weight
    if len(c) > 0:
        children = c[0].split(', ')
        for child in children:
            if not child in progs:
                progs[child] = prog(child)
            progs[child].parent = name
            progs[name].children.add(progs[child])
                
root = [pr.name for pr in progs.values() if pr.parent == None][0]
new_weight = [pr.unbalanced_child for pr in progs.values() if pr.unbalanced_child > 0][0]
            
print("Part 1: " + root)
print("Part 2: " + str(new_weight))