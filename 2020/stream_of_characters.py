"""
https://leetcode.com/problems/stream-of-characters/
"""


from typing import List, Deque
from collections import deque


class Trie:
    """
    Implementation of a prefix tree.
    """

    def __init__(self):
        self.root = {}

    def add_word(self, w: str) -> None:
        currNode = self.root
        for c in w:
            if c not in currNode:
                currNode[c] = {}

            currNode = currNode[c]

        currNode['#'] = True  # Mark the word end.

    def search_word(self, q: Deque[str]) -> bool:
        currNode = self.root
        for c in q:
            if c not in currNode:
                return False

            currNode = currNode[c]
            if '#' in currNode:
                return True

        return '#' in currNode


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        maxLen = 0
        for w in words:
            maxLen = max(maxLen, len(w))
            self.trie.add_word(w[::-1])  # Add the reversed word to the trie.

        self.preLetters = deque(maxlen=maxLen)

    def query(self, letter: str) -> bool:
        self.preLetters.appendleft(letter)
        return self.trie.search_word(self.preLetters)


s = StreamChecker(['cd', 'f', 'kl'])
print(s.query('a'))
print(s.query('b'))
print(s.query('c'))
print(s.query('d'))
print(s.query('e'))
print(s.query('f'))
print(s.query('g'))
print(s.query('h'))
print(s.query('i'))
print(s.query('j'))
print(s.query('k'))
print(s.query('l'))
