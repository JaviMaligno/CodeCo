from solution import Menu
import unittest

class MenuTests(unittest.TestCase):

    
    def test1(self):
        result = Menu()
        self.assertEqual(result.possible_choices([ 3, 3, 3 ], [ "1.1+2.1", "2.2-0.1" ]), 19)

    def test2(self):
        result = Menu()
        self.assertEqual(result.possible_choices([ 1, 2, 3 ], [ "1.1+0.0", "2.1+0.0" ]), 6)

    def test3(self):
        result = Menu()
        self.assertEqual(result.possible_choices([ 1, 2, 3 ], [ "1.1+0.0", "1.1+2.1", "2.1+0.0" ]), 3)
    def test4(self):
        result = Menu()
        self.assertEqual(result.possible_choices([ 1, 2, 3 ], [ "1.1+0.0", "2.1-0.0" ]), 4)

if __name__ == '__main__':
    unittest.main()