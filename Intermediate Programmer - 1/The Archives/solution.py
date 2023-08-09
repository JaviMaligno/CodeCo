import re
class Solution:
    pattern = "[0-9]-[0-9]{2}-[0-9]{6}-."
    def get_check_digit(self, code):
        # Your code goes here
        if not self.check_format(code):
            return -1
        else:
            numbers = [a for a in code[:-2] if a!="-"]
            number = sum([int(c)*(w+1) for w,c in enumerate(numbers)])%11
            
        return number
        
    def check_format(self, code):
        return re.match(self.pattern, code)