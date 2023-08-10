from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.jumble_sentence ("The cat sat on the Ikea mat."), "Eht act ast no eht Aeik amt.")
        
    def test2(self):
        result = Solution()
        self.assertEqual(result.jumble_sentence ("I'm John Q."), "I'm Hjno Q.")
    
    def test3(self):
        result = Solution()
        self.assertEqual(result.jumble_sentence ("Hello! - She said"), "Ehllo! - Ehs adis")

if __name__ == '__main__':
    unittest.main()