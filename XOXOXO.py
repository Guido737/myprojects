import random


def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 5)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose a cell (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("This cell is already taken, try another one.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")


def computer_move(board, player):
    while True:
        move = random.randint(0, 8)
        row, col = divmod(move, 3)
        if board[row][col] == ' ':
            board[row][col] = player
            print(f"Computer chose cell {move + 1}")
            break


def play_game(mode):
    board = [[' ' for i in range(3)] for i in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        if mode == 'player_vs_player' or (mode == 'player_vs_computer' and current_player == 'X'):
            player_move(board, current_player)
        else:
            computer_move(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'



def main():
    mode = input("With whom you want to play \n1) with another player \n2)With computer.\nEnter your choose: ")
    
    if mode == '1':
        play_game(mode='player_vs_player')
    elif mode == '2':
        play_game(mode='player_vs_computer')
    else:
        print("Invalid input. Try again.")
        main()
        
if __name__ == "__main__":
    main()
