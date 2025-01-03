

#Implementing tic-tac toe game
import math

# Board is represented as a list of 9 elements, initially empty
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check if there is a winner
def winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all([board[i] == player for i in condition]):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to make a move
def make_move(board, move, player):
    board[move] = player

# Minimax function to find the best move
def minimax(board, depth, is_maximizing):
    if winner(board, 'O'):  # AI wins
        return 1
    if winner(board, 'X'):  # Player wins
        return -1
    if is_board_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Main game loop
def play_game():
    while True:
        print_board(board)

        # Player's move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        make_move(board, move, 'X')

        if winner(board, 'X'):
            print_board(board)
            print("Player wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's move
        print("AI is making a move...")
        ai_move = find_best_move(board)
        make_move(board, ai_move, 'O')

        if winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()

# Implementing vaccum cleaner agent
def vacuum_cleaner_agent(location, status):
    x, y = location
    if status[x][y] == 'Dirty':
        return f"The vacuum cleaner is at ({x}, {y}) and it is dirty. Cleaning."
    else:
        return f"The vacuum cleaner is at ({x}, {y}) and it is clean. Moving."

status = [['Dirty', 'Clean'], ['Dirty', 'Dirty']]
location = (0, 0)

while True:
    action = vacuum_cleaner_agent(location, status)
    print(action)

    x, y = location
    if status[x][y] == 'Dirty':
        status[x][y] = 'Clean'

    if status[0][0] == 'Clean' and status[0][1] == 'Clean' and status[1][0] == 'Clean' and status[1][1] == 'Clean':
        print("All locations are clean. The vacuum cleaner is finished.")
        break

    if y < 1:
        location = (x, y + 1)
    elif x < 1:
        location = (x + 1, 0)
