from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.maximal_product(8), 18)
    def test2(self):
        result = Solution()
        self.assertEqual(result.maximal_product(7), 12)
    def test3(self):
        result = Solution()
        self.assertEqual(result.maximal_product(9), 27)

if __name__ == '__main__':
    unittest.main()