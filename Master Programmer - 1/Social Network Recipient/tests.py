from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.get_recipient("@JoeBloggs yo", 1), "JoeBloggs")

    def test2(self):
        result = Solution()
        self.assertEqual(result.get_recipient("Hey @Joe_Bloggs what time are we meeting @FredBloggs?", 2), "FredBloggs")
    
    def test3(self):
        result = Solution()
        self.assertEqual(result.get_recipient("hey@me.com, @JoeBloggs yo", 1), "JoeBloggs")
    
    def test4(self):
        result = Solution()
        self.assertEqual(result.get_recipient("hey@me.com, @JoeBloggs yo", 2), "")

if __name__ == '__main__':
    unittest.main()