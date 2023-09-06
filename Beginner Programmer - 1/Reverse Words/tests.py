from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.reverse_words("the quick brown fox"), "fox brown quick the")

if __name__ == '__main__':
    unittest.main()