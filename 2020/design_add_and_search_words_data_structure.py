"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


from collections import deque


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currNode = self.root
        for c in word:
            if c not in currNode:
                currNode[c] = {}

            currNode = currNode[c]

        currNode[' '] = {}  # Indicate the end of the word.

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to represent any one letter.
        """
        n, queue = len(word), deque([(0, self.root)])
        while queue:
            i, currNode = queue.popleft()
            if i == n:
                if ' ' in currNode:
                    return True
            else:
                currChar, nextLevel = word[i], i + 1
                if currChar == '.':
                    for nextNode in currNode.values():
                        queue.append((nextLevel, nextNode))
                else:
                    if currChar in currNode:
                        queue.append((nextLevel, currNode[currChar]))

        return False
