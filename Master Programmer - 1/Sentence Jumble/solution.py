class Solution:
    punctuation = [".", ",", ":", ";", "'", "?", "!", "-", "(", ")", "...", " "]
    def jumble_sentence (self, sentence):
        # Your code goes here
        punctuation_indices = [i for i,l in enumerate(sentence) if l in self.punctuation]
        chunks = zip([0]+punctuation_indices, punctuation_indices+[len(sentence)])
        jumbled_words = []
        for a,b in chunks:
            word = sentence[a:b] # the punctuation mark remains at the beginning, but punctuation marks have lower ordinal than letters so they are kept after sorting
            jumbled_word = self.jumble_word(word)
            jumbled_words.append(jumbled_word)
        return "".join(jumbled_words)
        
    def jumble_word(self, word):
        upper_indices = [i for i,l in enumerate(word) if l.isupper()]
        jumbled_word = "".join(sorted(word.lower())) 
        for index in upper_indices:
            jumbled_word = jumbled_word[:index]+jumbled_word[index].upper()+jumbled_word[index+1:]
        return jumbled_word
        