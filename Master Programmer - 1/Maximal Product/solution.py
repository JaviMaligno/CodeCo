class Solution:

    def maximal_product(self, input_number):
        # The solution is partitioning in the most 3's possible and filling with 2's
        # See this an related answers https://math.stackexchange.com/questions/125065/partitioning-a-natural-number-n-in-order-to-get-the-maximum-product-sequence-o
        if input_number < 2:
            return 0
        elif input_number % 3 == 0:
           return 3**(input_number // 3)
        elif input_number % 3 == 2:
            return 2*3**((input_number - 2)//3)
        else:
            return 4*3*((input_number-4)//3)