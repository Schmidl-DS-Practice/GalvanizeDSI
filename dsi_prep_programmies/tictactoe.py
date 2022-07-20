player_dict = {1: ' X ', 2: ' O '}

#create board
def initialize_board():
    return [[(i, j) for i in range(3)] for j in range(3)]

def print_board(board):
    for row in board:
       print(row)

#check for good coordinates
def get_check_coord(coord, board):
    if len(coord) != 2:
        print('You need to enter two coordinates. Try again.')
        return (False,)
    x, y = coord
    if x.isdigit() and y.isdigit():
        x, y = int(x), int(y)
    else:
        print('Please enter numbers for coordinates. Try again.')
        return (False,)
    if x > 2 or x < 0 or y > 2 or y < 0:
        print('Illegal coordinate. Try again')
        return (False,)
    if board[y][x] in [' X ', ' O ']:
        print('That square has already been played in. Try again.')
        return (False,)
    return x, y, True

#take the good coordinates
def get_good_coord(player, board):
    while True:
        play_prompt = 'Player {} ({}), where will you play? '
        coord = tuple(input(play_prompt.format(player, player_dict[player])).split(', '))
        stuff = get_check_coord(coord, board)
        if stuff[-1]:
            break
    return stuff[0], stuff[1]

#check for a winer
def check_winner(board, player):
    piece = player_dict[player]
    for i in range(3):
        if all([j == piece for j in board[i]]):
            return True
    for i in range(3):
        if all([board[j][i] == piece for j in range(3)]):
            return True
    if all([board[i][i] == piece for i in range(3)]):
        return True
    if all([board[i][2-i] == piece for i in range(3)]):
        return True
    return False

# play a turn
def play_turn(turn, board):
    player = turn % 2 + 1
    x, y = get_good_coord(player, board)
    board[y][x] = player_dict[player]
    winner = check_winner(board, player)
    return winner, player


def play_tic_tac_toe():
    board = initialize_board()
    print_board(board)
    for turn in range(9):
        winner, player = play_turn(turn, board)
        print_board(board)
        if winner:
            print('Player {} Wins!!'.format(player))
            break
    else:
        print('Game resulted in a tie...like usual.')


if __name__ == '__main__':
    play_tic_tac_toe()