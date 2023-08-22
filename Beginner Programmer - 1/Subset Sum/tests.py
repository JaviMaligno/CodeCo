from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.subset_sum([ 1, 0, -3, 5, 3 ]), True)

    def test2(self):
        result = Solution()
        self.assertEqual(result.subset_sum([ 1, 2, 3, 4, 5 ]), False)

if __name__ == '__main__':
    unittest.main()