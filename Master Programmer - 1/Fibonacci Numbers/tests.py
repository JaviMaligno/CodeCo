from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.is_fibonacci(3), True)

    def test2(self):
        result = Solution()
        self.assertEqual(result.is_fibonacci(6), False)

if __name__ == '__main__':
    unittest.main()