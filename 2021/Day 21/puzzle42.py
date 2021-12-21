from collections import defaultdict

# Player 1 starting position: 7
# Player 2 starting position: 5

# each turn 27 possibilities, but only 9 possible total spaces - range(3, 10)
# map: 3 - 1 universe
#      4 - 3
#      5 - 6
#      6 - 7
#      7 - 6
#      8 - 3
#      9 - 1

roll_prob = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]

# states track (p1_space, p1_score, p2_space, p2_score)
states = {(7, 0, 5, 0): 1}

wins = [0, 0]
p1 = True
while len(states) > 0:
    new_states = defaultdict(int)
    for s in states.keys():
        for roll in range(3,10):
            num_rolls = states[s] * roll_prob[roll]
            if p1:
                space = (s[0] + roll - 1) % 10 + 1 
                score = s[1] + space
                if score >= 21:
                    wins[0] += num_rolls
                else:
                    new_states[(space, score, s[2], s[3])] += num_rolls
            else:
                space = (s[2] + roll - 1) % 10 + 1 
                score = s[3] + space
                if score >= 21:
                    wins[1] += num_rolls
                else:
                    new_states[(s[0], s[1], space, score)] += num_rolls
    p1 = not p1
    states = new_states
    
print(max(wins))               