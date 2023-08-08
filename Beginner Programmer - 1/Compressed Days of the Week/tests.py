from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.compress_days([ "Su", "Mo", "Tu", "We" ]), "SMTW")

    def test2(self):
        result = Solution()
        self.assertEqual(result.compress_days([ "Fr", "Th", "Sa" ]), "TFS")
    
    def test3(self):
        result = Solution()
        self.assertEqual(result.compress_days([ "Fr", "Th", "Mo", "Tu", "We" ]), "D")
        
    def test4(self):
        result = Solution()
        self.assertEqual(result.compress_days([ "Fr", "Th", "Mo", "Tu", "We", "Sa", "Su" ]), "A")

    def test5(self):
        result = Solution()
        self.assertEqual(result.compress_days([  "Sa", "Su" ]), "E")
if __name__ == '__main__':
    unittest.main()