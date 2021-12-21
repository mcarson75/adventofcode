# Player 1 starting position: 7
# Player 2 starting position: 5

class player:
    def __init__(self, start):
        self.space = start
        self.rolls = 0
        self.score = 0
        
    def roll(self, spaces):
        self.space = (self.space + spaces - 1) % 10 + 1
        # mod = self.space % 10
        # self.spaces = 10 if mod == 0 else mod
        self.score += self.space
        self.rolls += 3
        
        return self.score >= 1000
        
p1 = player(7)
p2 = player(5)

die = list(range(1, 101))
for n in range(4):
    die += die

rolls = [sum(die[i:i+3]) for i in range(0, len(die), 3)]

i=0
while True:
    if p1.roll(rolls[i]):
        print(p2.score * (p1.rolls + p2.rolls))
        break
    if p2.roll(rolls[i+1]):
        print(p1.score * (p1.rolls + p2.rolls))
        break
    i += 2