finished = lambda s: all([c=='e' for c in s])

lines = [l.strip() for l in open("input.txt", 'r', encoding='utf-8').readlines()]
input = lines[-1]
lines = [l.split(' => ') for l in lines[:-2]]
repl = {r:l for l, r in lines}

key = sorted(repl.keys(), key=len, reverse=True)

steps = 0
while not finished(input):
    for n in range(len(input)):
        match = False
        for k in key:
            if input[-len(k)-n:len(input)-n] == k:
                steps += 1
                if n > 0:
                    input = input[:-len(k)-n] + repl[k] + input[-n:]
                else:
                    input = input[:-len(k)-n] + repl[k]
                print(input)
                match = True
        if match: break

print(steps)