import numpy as np

class bingo:
    def __init__(self, raw):
        self.board = []
        self.check = []
        for l in raw:
            self.board.append([int(x) for x in l.rstrip().split()])
        self.board = np.array(self.board)
        self.check = np.full_like(self.board, False)

    def set_num(self, num):
        self.check[np.where(self.board == num)] = True

    def winner(self):
        for row in self.check:
            if np.all(row):
                return True
        for col in range(0,len(self.check[0])):
            if np.all([row[col] for row in self.check]):
                return True
        return False

    def get_selected_total(self):
        return np.sum(self.board[np.where(self.check == False)])

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

numbers_called = [int(x) for x in lines[0].split(',')]

boards = []
input_line = 2

while input_line < len(lines):
    boards.append(bingo(lines[input_line:input_line+5]))
    input_line += 6

done = False
for num in numbers_called:
    for board in boards:
        board.set_num(num)
        if board.winner():
            print(num * board.get_selected_total())
            done = True
            break
    if done:
        break
