from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.match_adjacent("CAT", "SAD"), True)

    def test2(self):
        result = Solution()
        self.assertEqual(result.match_adjacent("FAT", "SAD"), False)
        
    def test3(self):
        result = Solution()
        self.assertEqual(result.match_adjacent("A", "A"), True)
    
    def test4(self):
        result = Solution()
        self.assertEqual(result.match_adjacent("A", "B"), True)
        
    def test5(self):
        result = Solution()
        self.assertEqual(result.match_adjacent("B", "A"), True)
    
    def test6(self):
        result = Solution()
        self.assertEqual(result.match_adjacent("B", "D"), False)
        
    def test7(self):
        result = Solution()
        self.assertEqual(result.match_adjacent("Z", "A"), False)
        
    def test8(self):
        result = Solution()
        self.assertEqual(result.match_adjacent("Z", "AB"), False)
if __name__ == '__main__':
    unittest.main()