from string import ascii_lowercase, ascii_uppercase

class Cipher:

    def halliday(self, message):
        # Your code goes here
        key = 13
        new_message = ""
        for letter in message:
            if letter.islower():
                alphabet = ascii_lowercase
                new_letter = self.caesar(ascii_lowercase, letter,13)
            elif letter.isupper():
                alphabet = ascii_uppercase
                new_letter = self.caesar(ascii_uppercase, letter,13)
            else:
                new_letter = letter
            
            new_message+= new_letter
                
            
        return new_message
    
    @staticmethod
    def caesar(alphabet, letter,key):
        l = len(alphabet)
        new_letter = alphabet[(alphabet.index(letter)+key)%l]
        return new_letter
        