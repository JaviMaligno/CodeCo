from math import sqrt
class Solution:

    def is_fibonacci(self, n):
        # Characterization of fibonacci numbers
        a = 5*n**2+4
        b = 5*n**2-4
        fibonacci = self.is_square(a) or self.is_square(b)
        return fibonacci
        
    def is_square(self,x):
        root = sqrt(x)
        return root == int(root)