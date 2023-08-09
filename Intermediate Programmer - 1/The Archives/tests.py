from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.get_check_digit("0-19-852663-x"), 6)
        
    def test1(self):
        result = Solution()
        self.assertEqual(result.get_check_digit("0-19-8526631-x"), -1)

if __name__ == '__main__':
    unittest.main()