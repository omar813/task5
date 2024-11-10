import unittest
from Calc import Cal

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = Cal.add(3, 7)
        self.assertEqual(result, 10)
        
        result = Cal.add(-1, 1)
        self.assertEqual(result, 0)
        
        result = Cal.add(-1, -1)
        self.assertEqual(result, -2)
