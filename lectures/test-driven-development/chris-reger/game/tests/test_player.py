import numpy as np
import unittest
import sys
sys.path.append('./src')
from player import Player
from die import Die

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.die = Die()
   
    def test_assignment_of_name(self):
        self.assertIsNotNone(self.player.name)

    def test_player_rolling_die(self):
        correct_values = list(range(1,self.die.n_sides+1)) 
        self.player.die = self.die
        num_rolls = 10 
        for _ in range(num_rolls):
            self.player.die.roll()
            self.assertIn(self.player.die.face_up, correct_values)

if __name__ == '__main__':
    unittest.main()

