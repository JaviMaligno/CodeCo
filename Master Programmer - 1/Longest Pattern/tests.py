from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.find_longest_pattern("acwxyzabghwxyo"), "wxyz")
        
    def test2(self):
        result = Solution()
        self.assertEqual(result.find_longest_pattern("azbycxdwev"), "")
    
    def test3(self):
        result = Solution()
        self.assertEqual(result.find_longest_pattern("abcaeabcaeabcdabcd"), "abcd")
        
    def test4(self):
        result = Solution()
        self.assertEqual(result.find_longest_pattern("abcaeabcaeAbcdabcd"), "Abcd")
    
    def test4(self):
        result = Solution()
        self.assertEqual(result.find_longest_pattern("abcaeabcaeabcdAbcd"), "abcd")

if __name__ == '__main__':
    unittest.main()