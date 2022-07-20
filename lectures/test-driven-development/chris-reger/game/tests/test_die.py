import numpy as np
import unittest
import sys
sys.path.append('./src')
from die import Die

class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = Die()
    
    def test_n_sides_default(self):
        self.assertEqual(self.die.n_sides, 6, 'default n incorrect')

    def test_roll(self):
        self.die.n_sides = 5
        correct_values = list(range(1,self.die.n_sides+1))
        num_rolls = 10 # number of rolls to test
        for _ in range(num_rolls):
            self.die.roll()
            self.assertIn(self.die.face_up, correct_values)

if __name__ == '__main__':
    unittest.main()

