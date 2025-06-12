import unittest
from util import multiply

class TestMultiplyFunction(unittest.TestCase):
    
    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3),6)
        
    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, -2), 4)
        
    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
