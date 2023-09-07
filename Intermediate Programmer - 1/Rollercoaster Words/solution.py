class Solution:

    def rollercoaster_word(self, input_string):
        # Your code goes here
        orders = list(map(ord, input_string.lower()))
        differences = [a-b for a,b in zip(orders[:-1],orders[1:])]
        for i in range(len(differences)-1):
            if differences[i]*differences[i+1]>0:
                return False
        return True