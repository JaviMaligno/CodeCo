class Solution:

    def duplicate_characters(self, input_string):
        # Your code goes here
        characters = set(input_string)
        return len([a for a in characters if input_string.count(a) > 1])