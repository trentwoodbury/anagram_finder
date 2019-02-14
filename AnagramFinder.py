# Package imports
from collections import Counter

# Local imports
from AnagramChecker import AnagramChecker

class AnagramFinder(AnagramChecker):
    '''
    This is a class that checks a word for any possible anagrams. It uses the words in
    english_words.txt to search for these anagrams. english_words.txt was sourced from
    https://github.com/dwyl/english-words.
    '''

    def __init__(self, verbose=False):
        '''
        verbose: Boolean. If true, we print function completion and results.
        '''
        self.anagrams = []
        self.words_are_anagrams = None
        self.verbose = verbose


    def get_dictionary(self):
        '''
        Creates dictionary mapping from first letter of word to word
        and word dictionary (mapping from each letter to number of occurrences)
        OUTPUT:
            word_dictionary: {first_letter: (word, Counter(word))}
        '''
        word_dictionary = {}
        with open('english_words.txt', 'r') as word_list:
            for word in word_list:
                cleaned_word = word.replace("\r\n", "")
                try:
                    word_dictionary[word[0]].append((cleaned_word, Counter(cleaned_word)))
                except:
                    word_dictionary[word[0]] = [(cleaned_word, Counter(cleaned_word))]
        self.word_dictionary = word_dictionary
        if self.verbose:
            print("Created word dictionary.")


    def search_for_anagrams(self, word):
        '''
        Searches self.word_dictionary for any words that are anagrams of word.
        INPUT
            word: string. The word we're searching for anagrams for.
        OUTPUT
            anagrams: list of anagramatic words.
        '''
        # handle prerequisites
        try:
            _ = self.word_dictionary
        except:
            self.get_dictionary()

        word_counter = Counter(word)
        anagrams = []
        for letter, frequency in word_counter.items():
            for pair_word in self.word_dictionary[letter]:
                pair_word_counter = pair_word[1]
                are_anagrams = self.check_if_words_are_anagram(pair_word_counter, word_counter)
                if are_anagrams and pair_word[0] != word:
                    anagrams.append(pair_word[0])

        self.anagrams = anagrams
        if self.verbose:
            print("Anagrams: {}".format(self.anagrams))
