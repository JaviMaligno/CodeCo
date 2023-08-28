from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.split_array([ 1, 3, 3, 4, 5 ]), True)

    def test2(self):
        result = Solution()
        self.assertEqual(result.split_array([ 2, 4, 5, 6 ]), False)

if __name__ == '__main__':
    unittest.main()