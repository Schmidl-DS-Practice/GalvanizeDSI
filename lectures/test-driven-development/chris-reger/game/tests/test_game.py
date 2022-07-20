import numpy as np
import unittest
import sys
sys.path.append('./src')
from player import Player
from die import Die
import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.die1 = Die(n_sides=20)
        self.player1 = Player(name='Bob', die=self.die1)
        self.die2 = Die(n_sides=4)
        self.player2 = Player(name='Sarah', die=self.die2)

    def test_play_the_game(self):
        game.play_the_game(self.player1, self.player2)
        self.assertIsNotNone(self.player1.die.face_up)
        self.assertIsNotNone(self.player2.die.face_up)

    def test_evaluate_winner(self):
        self.player1.die.face_up = 1
        self.player2.die.face_up = 1
        result = game.evaluate_winner(self.player1, self.player2)
        self.assertEqual(result, "It was a tie!")
        self.player1.die.face_up = 1
        self.player2.die.face_up = 2
        result = game.evaluate_winner(self.player1, self.player2)
        self.assertEqual(result, "Sarah won!")
        self.player1.die.face_up = 2
        self.player2.die.face_up = 1
        result = game.evaluate_winner(self.player1, self.player2)
        self.assertEqual(result, "Bob won!")

if __name__ == '__main__':
    unittest.main()

