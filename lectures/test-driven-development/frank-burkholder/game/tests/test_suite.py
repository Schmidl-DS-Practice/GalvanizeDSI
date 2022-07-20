import unittest
import sys
sys.path.append('./tests')
import test_die
import test_player
import test_game

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_die))
suite.addTests(loader.loadTestsFromModule(test_player))
suite.addTests(loader.loadTestsFromModule(test_game))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
