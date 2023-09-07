from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.rollercoaster_word("Bat"), True)

    def test2(self):
        result = Solution()
        self.assertEqual(result.rollercoaster_word("Bet"), False)

if __name__ == '__main__':
    unittest.main()