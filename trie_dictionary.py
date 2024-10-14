from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.root = TrieNode()
        pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        for word_frequency in words_frequencies:
            self.add_word_frequency(word_frequency)

    def goToWord(self, word):
        curNode = self.root
        for letter in word:
            children = curNode.children
            if letter in children:
                curNode = children[letter]
            else:
                return None
        return curNode

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        curNode = self.root
        for letter in word:
            children = curNode.children
            if letter in children:
                curNode = children[letter]
            else:
                return 0

        if curNode.is_last:
            return curNode.frequency
        return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        if self.search(word_frequency.word) == 0:
            curNode = self.root
            for letter in word_frequency.word:
                children = curNode.children
                if letter not in children:
                    children[letter] = TrieNode(letter)
                curNode = children[letter]
            curNode.frequency = word_frequency.frequency
            curNode.is_last = True
            return True
        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        curWord = self.goToWord(word)
        if curWord is None:
            return False
        if curWord.is_last:
            # if curWord.children is not None:
            curWord.is_last = False
            return True
            # else:
            #     curPre = None
            #     for letter in word:
            #         curPre += letter
            #         curLetter = self.goToWord(curPre)
            #         if len(curLetter.children)
        return False

    def tranverseTrie(self, node: TrieNode, word: str, array: list):
        # Method to recursively traverse the trie and return a whole word.
        if node is None:
            return 0
        if node.is_last:
            array.append(WordFrequency(word, node.frequency))
        for letter, child in node.children.items():
            self.tranverseTrie(child, word + letter, array)

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        tempList = []
        mainList = []
        curNode = self.goToWord(word)

        self.tranverseTrie(curNode, word, tempList)

        for i in range(0, 3):
            frequency = index = changeIndex = 0

            for word_frequency in tempList:
                if frequency < word_frequency.frequency:
                    frequency = word_frequency.frequency
                    addWord = word_frequency
                index += 1

            if not tempList:
                return mainList

            mainList.append(addWord)
            tempList.remove(addWord)
        return mainList
