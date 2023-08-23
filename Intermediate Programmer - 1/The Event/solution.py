class Solution:

    def calculate_difference(self, input_list):
        # Your code goes here
        maxim = self.compute_max(input_list)
        minim = self.compute_min(input_list)
        return maxim - minim
    
    def compute_max(self, input_list):
        return self.number_from_list(sorted(input_list, reverse = True))
    
    def compute_min(self, input_list):
        sort = sorted(input_list)
        if sort[0] > 0:
            return self.number_from_list(sort)
        else:
            return self.first_non_zero(sort)
        
    def first_non_zero(self,list_of_numbers):
        if all(x == 0 for x in list_of_numbers):
            return 0
        else:
            first_index = min(i for i,n in enumerate(list_of_numbers) if n > 0)
            new_list = [list_of_numbers[first_index]] + list_of_numbers[:first_index]+list_of_numbers[first_index+1:]
            return self.number_from_list(new_list)
            
    
    def number_from_list(self,list_of_numbers):
        return int("".join(map(str, list_of_numbers)))