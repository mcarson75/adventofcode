from itertools import combinations
import numpy as np

distance = lambda p, q: ((p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2)
manhattan = lambda p, q: abs(p[0]-q[0]) + abs(p[1]-q[1]) + abs(p[2]-q[2])

class scanner:
    def __init__(self, name):
        self.name = name
        self.beacons = set()
        self._p = None
        self._r = None
        self._d = None
        self._s = None

    shift = lambda self, pt1, pt2: (pt2[0]-pt1[0], pt2[1]-pt1[1], pt2[2]-pt1[2])
    add = lambda self, pt1, pt2: (pt2[0]+pt1[0], pt2[1]+pt1[1], pt2[2]+pt1[2])
    
    @property
    def position(self): return self._p
    
    @position.setter
    def position(self, value):
        self._p = value
        if self.rotation != None:
            self.beacons = self._beacons_shift()
            self._d = self._distances()
            
    @property
    def rotation(self): return self._r
    
    @rotation.setter
    def rotation(self, value):
        self._r = value
        if self.position != None:
            self.beacons = self._beacons_shift()
            self._d = self._distances()

    def rotations(self):
        vectors = [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]
        vectors = list(map(np.array, vectors))
        for vi in vectors:
            for vj in vectors:
                if vi.dot(vj) == 0:
                    vk = np.cross(vi, vj)
                    yield lambda x: np.matmul(x, np.array([vi, vj, vk]))
                    
    @property
    def distances(self):
        if self._d is None:
            self._d = self._distances()
        return self._d
        
    def _distances(self):
        d = {}
        for p, q in combinations(self.beacons, 2):
            dist = distance(p, q)
            if p not in d:
                d[p] = set([dist])
            else:
                d[p].add(dist)
            if q not in d:
                d[q] = set([dist])
            else:
                d[q].add(dist)
        return d
    
    def match(self, other):
        pts = {}
        for p in self.beacons:
            for q in other.beacons:
                if len(self.distances[p] & other.distances[q]) >= 11:
                    pts[p] = q
        
        for rot in self.rotations():
            shift = set([self.shift(rot(v), k) for k, v in pts.items()])
            if len(shift) == 1:
                other.rotation = rot
                other.position = list(shift)[0]
                return True
                break
        
        return False
    
    def _beacons_shift(self):
        b = set()
        for s in self.beacons:
            b.add(self.add(self.rotation(s), self.position))
        return b

scanners = []
for line in open("input.txt", 'r', encoding='utf-8'):
    if 'scanner' in line:
        s = [int(i) for i in line.strip().split() if i.isnumeric()][0]
        scanners.append(scanner(s))
    elif line != '\n':
        coord = [int(i) for i in line.strip().split(',')]
        scanners[s].beacons.add(tuple(coord))

scanners[0].position = (0, 0, 0)
scanners[0].rotation = lambda x: np.matmul(x, np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

known = [s for s in scanners if s.position != None]
unknown = [s for s in scanners if s.position == None]

while True:
    if len(unknown) == 0: break
    for u in unknown:
        for k in known:
            if k.match(u):
                known.append(u)
                unknown.remove(u)
                break
    
farthest = max([manhattan(p.position, q.position) for p, q in combinations(scanners, 2)])

print(farthest)