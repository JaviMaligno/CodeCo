class Solution:

    def calculate_rats_value(self, input_value):
        # Your code goes here
        too_large = 4294967296
        if input_value < 0 or input_value > too_large:
            return -1
        next = int("".join(sorted(str(input_value +int(str(input_value)[::-1])))))
        return next if 0 < next < too_large else -1
        