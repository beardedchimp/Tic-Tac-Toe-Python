import random


# Display the visual aspect of the board
def display_board(board):
    print("  " + " | " + " " + " | " + " ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("  " + " | " + " " + " | " + " ")
    print("-----------")
    print("  " + " | " + " " + " | " + " ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("  " + " | " + " " + " | " + " ")
    print("-----------")
    print("  " + " | " + " " + " | " + " ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("  " + " | " + " " + " | " + " ")


# Test array board used for debugging
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

# display_board(test_board)


# Sets up both players markers as either X or O
def player_input():
    player1_marker = ''
    player2_marker = ''
    while player1_marker != 'X' and player1_marker != 'O':
        player1_marker = input("Player 1, choose X or O\n").upper()

    if player1_marker == 'X':
        player2_marker = 'O'
        print(f"Player 1 has chosen to be {player1_marker}. Player 2 will be playing {player2_marker}.")
        return 'X', 'O'
    else:
        player2_marker = 'X'
        print(f"Player 1 has chosen to be {player1_marker}. Player 2 will be playing {player2_marker}.")
        return 'O', 'X'


# player_input()


# Places a player's X or O onto the board
def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board, '$', 8)
# display_board(test_board)


# Determines if there is a winner based on if there are 3 markers in a row horizontally, vertically, or diagonally
def win_check(board, marker):
    if (board[1] == board[2] == board[3] == marker or board[4] == board[5] == board[6] == marker or
            board[7] == board[8] == board[9] == marker or board[1] == board[4] == board[7] == marker or
            board[2] == board[5] == board[8] == marker or board[3] == board[6] == board[9] == marker or
            board[1] == board[5] == board[9] == marker or board[3] == board[5] == board[7] == marker):
        return True
    else:
        return False


# win_check(test_board, 'X')


# Randomly determines who will be the first player
def choose_first():
    if random.randint(1, 2) == 1:
        print("X will go first.")
    else:
        print("O will go first.")


# Determines if the selected position is a valid and empty position
def space_check(board, position):
    if board[position] != ' ':
        return False
    else:
        return True


# Determines if the board is currently full, which would mean that the game is a Tie
def full_board_check(board):
    for n in board:
        if n == ' ':
            return False
        else:
            return True


# Asks a player for their board position and determines if that spot is valid through space_check
def player_choice(board):
    chosen_position = int(input("Where would you like to go next (1-9)?\n"))
    while not space_check(board, chosen_position):
        chosen_position = int(input("That was not a valid position, please choose an open spot between (1-9)\n"))
    return chosen_position


# Asks the players if they would like to play again, defaults to No if anything other than a Y is entered
def replay():
    if input("Would you like to play again (Y/N)?\n").upper() == 'Y':
        return True
    else:
        return False


# Main game routine
print("Welcome to Tic Tac Toe!")

while True:
    game_board = [' ']*10
    player1_marker, player2_marker = player_input()

    game_on = True
    while game_on:
        # Player 1 Turn
        display_board(game_board)
        player_position = player_choice(game_board)
        place_marker(game_board, player1_marker, player_position)
        if win_check(game_board, player1_marker):
            display_board(game_board)
            print("Player 1 Wins!")
            game_on = False
            break
        elif full_board_check(game_board):
            display_board(game_board)
            print("It is a Tie!")
            game_on = False
            break
        else:
            pass

        # Player2's turn.
        display_board(game_board)
        player_position = player_choice(game_board)
        place_marker(game_board, player2_marker, player_position)
        if win_check(game_board, player2_marker):
            display_board(game_board)
            print("Player 2 Wins!")
            game_on = False
            break
        elif full_board_check(game_board):
            display_board(game_board)
            print("It is a Tie!")
            game_on = False
            break
        else:
            pass

    if not replay():
        break
