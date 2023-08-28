from itertools import chain, combinations
class Solution:

    def split_array(self, input_array):
        # Your code goes here
        numbers = input_array
        subsets = list(self.truncated_powerset(input_array))
        for subset in subsets:
            comp = self.complement(subset, numbers)
            if sum(subset) == sum(comp):
                break
        else:
            return False
        return True
    
    def truncated_powerset(self,iterable):
        l = len(iterable)
        return chain.from_iterable(combinations(iterable, r) for r in range((l+1)//2))
        
    def complement(self,sublist,main_list):
        complement = main_list[:]
        for element in sublist:
            complement.remove(element)
        return complement