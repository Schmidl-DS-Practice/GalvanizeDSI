# requirement:
# test if a sequence of at least three integers
# in a list is a Fibonacci sequence

# code is in fibonacci.py
import fibonacci
import unittest


class TestFibonacci(unittest.TestCase):
    def test_is_fibonacci(self):
        self.assertEqual(fibonacci.is_fibonacci([1,1,2,3]), True)
        self.assertEqual(fibonacci.is_fibonacci([1,1,2,4]), False)
        self.assertEqual(fibonacci.is_fibonacci([0,1,1]), True)
        self.assertEqual(fibonacci.is_fibonacci([34,55,89,144,233]), True)

if __name__ == '__main__':
    unittest.main()
    
