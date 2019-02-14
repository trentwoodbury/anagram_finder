from collections import Counter

class AnagramChecker:
    '''
    This is a class that is able to efficiently check if two words are anagrams.
    '''

    def __init__(self):
        self.words_are_anagrams = None

    def check_if_words_are_anagram(self, word_1, word_2):
        '''
        Checks if word_1 and word_2 are anagrams. Returns True of False.
        INPUT
            word_1, word_2: Counter(word). They look like e.g. {'a':3, 'b':1, 'n':2}
        OUTPUT
            True/False: whether words are anagrams.
        '''
        # If words have different number of unique letters, they aren't anagrams
        if len(word_1.items()) != len(word_2.items()):
            return False
        else:
            for letter, frequency in word_1.items():
                try:
                    if word_2[letter] == frequency:
                        pass
                    else:
                        return False
                except:
                    return False
            return True
