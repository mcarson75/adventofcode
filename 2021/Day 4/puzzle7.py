import numpy as np

def check_board(board):
    for row in board:
        if np.all(row):
            return True
    for col in range(0,len(board[0])):
        if np.all([row[col] for row in board]):
            return True
        
    return False

with open('input.txt', 'r', encoding='utf-8') as read_file:
    lines = read_file.readlines()

numbers_called = [int(x) for x in lines[0].split(',')]

boards = []

input_line = 2
while input_line < len(lines):
    this_board = []
    board = lines[input_line:input_line+5]
    for b in board:
        this_line = [int(x) for x in b.rstrip().split()]
        this_board.append(this_line)
    boards.append(this_board)
    input_line += 6

boards = np.array(boards)
checks = np.full_like(boards, False)
done = False

for num in numbers_called:
    for n in range(0, len(boards)):
        board = boards[n]
        check = checks[n]
        check[np.where(board==num)] = True
        if check_board(check):
            final_board = board
            final_check = check
            done = True
            break
    if done:
        break
    
print(num)
print(final_board)
print(final_check)

non_selected_total = np.sum(final_board[np.where(final_check==False)])
print(non_selected_total)
print(non_selected_total*num)

