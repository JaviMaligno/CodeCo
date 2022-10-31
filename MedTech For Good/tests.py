from solution import MedicalImaging
import unittest

class MedicalImagingTests(unittest.TestCase):

    
    def test1(self):
        result = MedicalImaging()
        self.assertEqual(result.match_patterns([ " xx    x ", "   xx    ", "    x x  ", "   x  xx ", " xxx     " ], [ "x ", "xx" ]), 3)

    def test2(self):
        result = MedicalImaging()
        self.assertEqual(result.match_patterns([ "         ", "    *  **", "  ****   ", "    *    ", "   ***   " ], [ " * ", "***", " * " ]), 1)

if __name__ == '__main__':
    unittest.main()