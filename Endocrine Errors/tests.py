from solution import Dialysis
import unittest

class DialysisTests(unittest.TestCase):

    
    def test1(self):
        result = Dialysis()
        self.assertEqual(result.analyse(100, [ 0, 0, 1, 10, 20, 40, 80, 70, 80, 90, 100 ]), 2)

    def test2(self):
        result = Dialysis()
        self.assertEqual(result.analyse(100, [ 90, 95, 98, 99, 99.5, 100, 100, 101, 97, 99, 100 ]), 3)

if __name__ == '__main__':
    unittest.main()