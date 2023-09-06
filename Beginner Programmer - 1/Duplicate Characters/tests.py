from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.duplicate_characters("Aasdefsgh!!"), 2)

if __name__ == '__main__':
    unittest.main()