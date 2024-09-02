# your code goes here!
class Anagram:
    def __init__(self, word):
        self.base_word = word
    
    def match(self, possible_anagrams):
        # Sort the letters of the base_word
        sorted_base_word = ''.join(sorted(self.base_word))
        matches = []
        for word in possible_anagrams:
            # Sort the letters of the current word
            if ''.join(sorted(word)) == sorted_base_word:
                matches.append(word)
        return matches
