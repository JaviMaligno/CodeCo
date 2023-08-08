from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.calculate_pascal_layer_total (0), 1)

    def test2(self):
        result = Solution()
        self.assertEqual(result.calculate_pascal_layer_total (1), 2)

    def test2(self):
        result = Solution()
        self.assertEqual(result.calculate_pascal_layer_total(-1), 0)

if __name__ == '__main__':
    unittest.main()