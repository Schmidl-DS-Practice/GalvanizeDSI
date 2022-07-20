from die import Die
from player import Player

def evaluate_winner(player1, player2):
    if player1.die.face_up != player2.die.face_up:
        if player1.die.face_up > player2.die.face_up:
            winner_str = (f"{player1.name} won!")
        else:
            winner_str = (f"{player2.name} won!")
    else:
        winner_str = ("It was a tie!")
    return winner_str

def play_the_game(player1, player2):
    player1.die.roll()
    player2.die.roll()
    print(f"{player1.name} rolled a {player1.die.face_up}.")
    print(f"{player2.name} rolled a {player2.die.face_up}.")

if __name__ == '__main__':
    die1 = Die(n_sides=8)
    player1 = Player(name='Frank', die=die1)

    die2 = Die(n_sides=4)
    player2 = Player(name='Josh', die=die2)

    play_the_game(player1, player2)
    winner = evaluate_winner(player1, player2)
    print(winner)
