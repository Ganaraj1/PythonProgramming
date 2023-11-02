import random

def print_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def choose_marker():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to be X or O? ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

def is_board_full(board):
    return all(x != ' ' for x in board)

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not is_space_free(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def is_space_free(board, position):
    return board[position] == ' '

def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if possible_moves:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_move(board, computer_marker):
    if computer_marker == 'X':
        player_marker = 'O'
    else:
        player_marker = 'X'

    # Check if computer can win in the next move
    for i in range(1, 10):
        copy = board[:]
        if is_space_free(copy, i):
            place_marker(copy, computer_marker, i)
            if win_check(copy, computer_marker):
                return i

    # Check if the player could win on their next move and block them.
    for i in range(1, 10):
        copy = board[:]
        if is_space_free(copy, i):
            place_marker(copy, player_marker, i)
            if win_check(copy, player_marker):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def play_game():
    print('Welcome to Tic Tac Toe!')
    while True:
        the_board = [' '] * 10
        player1_marker, player2_marker = choose_marker()
        turn = 'Player 1'
        game_on = True

        while game_on:
            if turn == 'Player 1':
                print_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    print_board(the_board)
                    print('Congratulations! Player 1 has won the game!')
                    game_on = False
                else:
                    if is_board_full(the_board):
                        print_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                print_board(the_board)
                position = get_computer_move(the_board, player2_marker)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    print_board(the_board)
                    print('Computer has won!')
                    game_on = False
                else:
                    if is_board_full(the_board):
                        print_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            break

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

if __name__ == '__main__':
    play_game()