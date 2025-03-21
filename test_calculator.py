#create a unit test for the calculator

import unittest

from calculator import multiply

class TestCalculator(unittest.TestCase):
    
        def test_multiply(self):
            self.assertEqual(multiply(2, 3), 6)
            self.assertEqual(multiply(1, 0), 0)
            self.assertEqual(multiply(0, 0), 0)
            self.assertEqual(multiply(-1, 1), -1)
            self.assertEqual(multiply(-1, -1), 1)
            self.assertEqual(multiply(1.5, 2), 3)
            self.assertEqual(multiply(1.5, 2.5), 3.75)
            self.assertEqual(multiply(1.5, -2.5), -3.75)
            self.assertEqual(multiply(-1.5, -2.5), 3.75)

if __name__ == "__main__":
    unittest.main()