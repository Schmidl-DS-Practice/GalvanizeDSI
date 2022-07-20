import random

class Die(object):
    def __init__(self, n_sides=6):
        self.n_sides = n_sides

    def roll(self):
       self.face_up = random.randint(1,self.n_sides)

if __name__ == '__main__':
    die = Die()
    die.roll()
    print(f"The {die.n_sides} sided die rolled a {die.face_up}")
