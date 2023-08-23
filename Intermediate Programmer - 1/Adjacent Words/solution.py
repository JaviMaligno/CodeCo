class Solution:

    def match_adjacent(self, input1, input2):
        # Your code goes here
        if len(input1) != len(input2):
            return False
        for letter1 in input1:
            adjacents = [letter2 for letter2 in input2 if self.adjacent_letters(letter1,letter2)]
            if len(adjacents) != 1:
                return False
        return True
    
    def adjacent_letters(self, letter1, letter2):
        return ord(letter1) - 1 <= ord(letter2) <= ord(letter1) + 1