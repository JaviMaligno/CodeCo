class Solution:

    def second_highest_digit(self, input_string):
        # Your code goes here
        digits = sorted(filter(lambda x: x.isdigit(), input_string), reverse=True)
        if len(digits) < 2:
            second = -1
        else:
            second = int(digits[1])
        return second