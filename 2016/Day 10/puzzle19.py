from collections import defaultdict
import typing

bots = defaultdict()
outputs = defaultdict()

class output:
    def __init__(self, num):
        self.num = num
        self._input = None
        self.defined = False
        
    @property
    def input(self):
        return self._input
    
    @input.setter
    def input(self, value):
        self._input = value
        self.defined = True
        
    @property
    def output(self):
        return self.input

class bot:
    def __init__(self, num):
        self.num : int = num
        self._input : set = set()
        self._low_bot : bot or output = None
        self._high_bot : bot or output = None
        self.low : int = None
        self.high : int = None
        self.defined : bool = False
    
    @property
    def input(self) -> set:
        return self._input
    
    @input.setter
    def input(self, value: int) -> None:
        self._input.add(value)
        if len(self.input) >= 2:
            self.low = min(self.input)
            self.high = max(self.input)
            self.give_values()
    
    @property
    def low_bot(self):
        return self._low_bot
    
    @low_bot.setter
    def low_bot(self, value):
        self._low_bot = value
        self.give_values()
            
    @property
    def high_bot(self):
        return self._high_bot
    
    @high_bot.setter
    def high_bot(self, value):
        self._high_bot = value
        self.give_values()

    def give_values(self):
        if self.low and self.low_bot and self.high and self.high_bot:
            self.defined = True
        if self.low and self.low_bot and not self.low_bot.defined:
            self.low_bot.input = self.low
        if self.high and self.high_bot and not self.high_bot.defined:
            self.high_bot.input = self.high

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = [s.rstrip() for s in f.readlines()]

def initialize_bot(b):
    if b not in bots:
        bots[b] = bot(b)

def initialize_output(b):
    if b not in outputs:
        outputs[b] = output(b)

n = 0
while True:
    line = lines[n]
    
    if 'value' in line:
        #value 31 goes to bot 114
        v, b = [int(s) for s in line.split() if s.isnumeric()]
        initialize_bot(b)
        bots[b].input = v
    else:
        # bot 59 gives low to bot 176 and high to bot 120
        _, b, _, _, _, tl, l, _, _, _, th, h = line.split()
        b, l, h = int(b), int(l), int(h)
        
        initialize_bot(b)
        if tl == 'bot':
            initialize_bot(l)
            bots[b].low_bot = bots[l]
        else:
            initialize_output(l)
            bots[b].low_bot = outputs[l]
        if th == 'bot':
            initialize_bot(h)
            bots[b].high_bot = bots[h]
        else:
            initialize_output(h)
            bots[b].high_bot = outputs[h]
            

    n += 1
    if n >= len(lines):
        if all([b.defined for b in bots.values()]): break
        n = 0

n = [b.num for b in bots.values() if b.low == 17 and b.high == 61][0]
        
print("bot: " + str(n))