from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(1), 2)

    def test2(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(2), 4)
        
    def test3(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(8), 16)
        
    def test4(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(16), 77)
    
    def test5(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(77), 145)  
    
    def test6(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(145), 668)  
        
    def test7(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(5566666667777), -1) 
        
    def test8(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(-1), -1) 
        
    def test9(self):
        result = Solution()
        self.assertEqual(result.calculate_rats_value(1233334444), -1) 
    

if __name__ == '__main__':
    unittest.main()