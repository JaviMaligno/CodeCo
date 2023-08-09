from solution import Cipher
import unittest

class CipherTests(unittest.TestCase):

    
    def test1(self):
        result = Cipher()
        self.assertEqual(result.halliday("Crystal Key"), "Pelfgny Xrl")

    def test2(self):
        result = Cipher()
        self.assertEqual(result.halliday("Orb of Osuvox"), "Beo bs Bfhibk")
        
    def test3(self):
        result = Cipher()
        self.assertEqual(result.halliday("ro** 237"), "eb** 237")
        
    def test4(self):
        result = Cipher()
        self.assertEqual(result.halliday("An**ak? $ millions?!"), "Na**nx? $ zvyyvbaf?!")
    
    def test5(self):
        result = Cipher()
        self.assertEqual(result.halliday("+- the_distracted_gl*** -+"), "+- gur_qvfgenpgrq_ty*** -+")

if __name__ == '__main__':
    unittest.main()