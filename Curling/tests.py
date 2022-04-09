from solution import Curling
import unittest


class CurlingTests(unittest.TestCase):

    def test1(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.6, -0.6, 1.4, 1.8), 2.09)

    def test2(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.5, 0, 1.8, 0.707), 4.74)

    def test3(self):
        solution = Curling()
        self.assertEqual(solution.push_stones(1.8, 0, 1.75, 0.5), -1)


if __name__ == '__main__':
    unittest.main()