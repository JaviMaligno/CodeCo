class Solution:

    def reverse_words(self, input_string):
        # Your code goes here
        return " ".join(input_string.split(" ")[::-1])