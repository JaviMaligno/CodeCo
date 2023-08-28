class Solution:

    def find_longest_pattern(self, input_string):
        # Your code goes here
        longest_pattern = ""
        current_pattern = ""
        for c in input_string:
            if not current_pattern:
                current_pattern+=c 
            elif ord(c.lower()) == ord(current_pattern[-1].lower())+1:
                current_pattern+=c 
            elif len(current_pattern) > len(longest_pattern):
                longest_pattern = current_pattern
                current_pattern = c
            else:
                current_pattern = c
        return longest_pattern if len(longest_pattern) > 1 else ""
    
if __name__ == "__main__":
    result = Solution()
    result.find_longest_pattern("abcaeabcaeabcdabcd")