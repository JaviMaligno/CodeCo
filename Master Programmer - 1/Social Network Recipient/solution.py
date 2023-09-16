import re 

class Solution:

    def get_recipient(self, message, position):
        # Your code goes here
        users = [re.match("^@[\w´-]+", word).group() for word in message.split() if word.startswith("@")]
        
        return users[position-1][1:] if 1 <= position <= len(users) else ""