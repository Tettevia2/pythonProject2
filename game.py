game_board = {'7': '', '8': '', '9': '',
              '4': '', '5': '', '6': '',
              '1': '', '2': '', '3': '', }
print(game_board)


def print_board(board):
    print('|' + board['7'] + '|' + board['8'] + '|' + board['9'] + '|')
    print('----')
    print('|' + board['4'] + '|' + board['5'] + '|' + board['6'] + '|')
    print('----')
    print('|' + board['1'] + '|' + board['2'] + '|' + board['3'] + '|')
    print('----')


print_board(game_board)

endgame = True
number_of_moves = 9
whos_turn = 'x'


def game(number_of_moves, whos_turn):
    print("It is", whos_turn, "turn to play : ")
    move = input()

    if game_board[move] != '':
        print(move, "has already been played.Select a different slot")
        move = input()
    else:
        game_board[move] = whos_turn

    print_board(game_board)


while number_of_moves > 0:
    if whos_turn == "o":
        whos_turn = "x"
    else:
        whos_turn = "o"

    game(number_of_moves, whos_turn)
    number_of_moves -= 1

    if number_of_moves <= 4:
        if game_board['7'] == game_board['8'] == game_board['9'] != '':
            print("Game Over", whos_turn, "wins")
            number_of_moves = 0
game(9,'x')