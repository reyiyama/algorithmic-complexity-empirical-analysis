from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.dict = []  # Initalize an empty list
        pass


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # Looping through list of WordFrequency objects to add into ArrayDictionary object
        for word_frequency in words_frequencies:
            self.add_word_frequency(word_frequency)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        for element in self.dict:
            if element.word == word:
                return element.frequency
            if element.word > word:
                return 0
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        index = 0
        if self.search(word_frequency.word) == 0:
            for key in self.dict:
                if word_frequency.word < key.word:
                    self.dict.insert(index, word_frequency)
                    return True
                index += 1
            self.dict.append(word_frequency)
            return True
        else:
            return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED
        for key in self.dict:
            if key.word == word:
                self.dict.remove(key)
                return True
        return False

    def searchPrefix(self, prefix, word):
        for i in range(0, len(prefix)):
            if i < len(word):
                if prefix[i] != word[i]:
                    return False
            else:
                return False
        return True

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        autoCompleteList = ArrayDictionary()
        autoCompleteListTemp = ArrayDictionary()

        if not self.dict:
            return autoCompleteList.dict

        for key in self.dict:
            if self.searchPrefix(prefix_word, key.word):
                autoCompleteListTemp.add_word_frequency(key)

        for i in range(0, 3):
            frequency = index = changeIndex = 0
            for key in autoCompleteListTemp.dict:
                if frequency < key.frequency:
                    frequency = key.frequency
                    changeIndex = index
                index += 1
            if not autoCompleteListTemp.dict:
                return autoCompleteList.dict
            autoCompleteList.dict.append(autoCompleteListTemp.dict[changeIndex])
            autoCompleteListTemp.delete_word(autoCompleteList.dict[i].word)

        return autoCompleteList.dict
