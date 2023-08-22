class Solution:

    def subset_sum(self, input_list):
        # Your code goes here
        visited = []
        for number in input_list:
            if -number in visited:
                return True
            else:
                visited.append(number)
                
        return False