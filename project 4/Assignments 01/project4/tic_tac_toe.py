import time

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_player_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Enter number between 1 and 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] != " ":
                print("Cell already taken. Choose another.")
                continue
            return row, col
        except ValueError:
            print("Please enter a valid number.")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_player_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"
        time.sleep(0.5)

if __name__ == "__main__":
    tic_tac_toe()
