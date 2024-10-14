from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency, next = None):
        self.word_frequency = word_frequency
        self.next = next

    def compPre(self, prefix, word):
        for i in range(0, len(prefix)):
            if i < len(word):
                if prefix[i] != word[i]:
                    return False
            else:
                return False
        return True

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.head = None
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
        curNode = self.head
        while curNode != None:
            if curNode.word_frequency.word == word:
                return curNode
            curNode = curNode.next
        return None

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        # TO BE IMPLEMENTED
        curNode = self.goToWord(word)
        if curNode is None:
            return 0
        else:
            return curNode.word_frequency.frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        if not self.head:
            self.head = ListNode(word_frequency)
            return True

        if self.search(word_frequency.word) == 0:
            self.head = ListNode(word_frequency, self.head)
            return True
        else:
            return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        # TO BE IMPLEMENTED
        curNode = self.head
        prevNode = None

        if curNode is None:
            return False

        if curNode.word_frequency.word == word:
            self.head = curNode.next
            return True
        while curNode != None:
            if curNode.word_frequency.word == word:
                prevNode.next = curNode.next
                del curNode
                return True
            else:
                prevNode = curNode
                curNode = curNode.next
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # TO BE IMPLEMENTED
        curNode = self.head
        tempList = []
        mainList = []
        while curNode is not None:
            if curNode.compPre(word, curNode.word_frequency.word):
                tempList.append(curNode.word_frequency)
            curNode = curNode.next

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


