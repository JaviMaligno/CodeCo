from solution import Slalom
import unittest


class SlalomTests(unittest.TestCase):

    def test1(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([10, -10, 10, -10, 10], 2), 81)

    def test2(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([-10, 5, -15, 0, -10, 10, -5], 3), 85.5)

    def test3(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([], 3), 0)

    def test4(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([-10, -9], 2), 9)

    def test5(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([0,10, 9], 2), 9)

    def test6(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([9], 3), 7.5)

    def test7(self):
        solution = Slalom()
        self.assertEqual(solution.total_displacement([9.33333], 3), 7.8333)



if __name__ == '__main__':
    unittest.main()