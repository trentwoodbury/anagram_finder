from collections import Counter

class AnagramChecker:
    '''
    This is a class that is able to efficiently check if two words are anagrams.
    '''

    def __init__(self, word_1, word_2):
        self.word_1 = word_1
        self.word_2 = word_2
        self.words_are_anagrams = None

    def check_if_words_are_anagram(self):
        word_1_counter = Counter(self.word_1)
        word_2_counter = Counter(self.word_2)
        # If words have different number of unique letters, they aren't anagrams
        if len(word_1_counter.items()) != len(word_2_counter.items()):
            self.words_are_anagrams = False
        else:
            for letter, frequency in word_1_counter.items():
                try:
                    if word_2_counter[letter] == frequency:
                        pass
                    else:
                        self.words_are_anagrams = False
                except:
                    self.words_are_anagrams = False
        if self.words_are_anagrams is None:
            self.words_are_anagrams = True
