from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.second_highest_digit("abc:1231234"), 3)

    def test2(self):
        result = Solution()
        self.assertEqual(result.second_highest_digit("123123"), 3)

    def test3(self):
        result = Solution()
        self.assertEqual(result.second_highest_digit("1"), -1)

if __name__ == '__main__':
    unittest.main()