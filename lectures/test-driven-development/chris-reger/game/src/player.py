from die import Die

class Player(object):
    def __init__(self, name='ReadyPlayer1', die=None):
        self.name = name
        self.die = die

if __name__ == '__main__':
    die = Die()
    player1 = Player(name='Bob', die=die)
    player1.die.roll()
    print(f"{player1.name} rolled a {player1.die.face_up}.")

