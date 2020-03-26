"""
https://leetcode.com/problems/palindrome-pairs/
"""


from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.nextNodes = defaultdict(TrieNode)
        self.wordEndInd = -1
        self.pIdxs = []


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def _is_palindrome(self, word: str, l: int, r: int) -> bool:
        """
        Check if word[l: r + 1] is a palindrome.
        """
        while l < r:
            if word[l] != word[r]:
                return False

            l += 1
            r -= 1

        return True

    def add_word(self, word: str, wordIdx: int):
        """
        Add the input word to the trie in reversed order.

        Add the index of the input word to self.pIdxs if:
        1. The current node is a word end.
        2. The word formed from the current node to the word end node below
           is a palindrome.

        For example, the input word list is ['abc', 'xyxabc']. Then the trie
        will look as below:
            root
            | c
            n1
            | b
            n2
            | a
            n3  [0, 1]
            | x
            n4
            | y
            n5
            | x
            n6 [1]

        When adding word 'abc', n3 will contain [0] as it is the word end node.

        When adding word 'xyxabc', n3 will contain [0, 1] as xyx is a
        palindrome, so the index of 'xyxabc', which in our case is 1, is added
        to the pIdxs of node n3.
        """
        currNode, maxLen = self.root, len(word)
        for i in reversed(range(maxLen)):
            c = word[i]
            if self._is_palindrome(word, 0, i):
                currNode.pIdxs.append(wordIdx)

            currNode = currNode.nextNodes[c]

        currNode.wordEndInd = wordIdx  # Mark the current node as the word end.
        currNode.pIdxs.append(wordIdx)  # Add the current index.

    def search_word(self, word: str, wordIdx: int) -> List[List[int]]:
        """
        Try to search palindrome pairs for the input word for the below cases:
        1. A1 + A2 forms input word A. A1 has a match B in input word list
            while A2 is already a palindrome. -> A is longer than B.

        2. B1 + B2 forms another word in the input word list. A matches B2
            while B1 is already a palindrome.  -> A is shorter than B.
        """
        currNode, rslt, maxLen = self.root, [], len(word) - 1
        for i, c in enumerate(word):
            if currNode.wordEndInd >= 0 and currNode.wordEndInd != wordIdx and\
                    self._is_palindrome(word, i, maxLen):
                """
                1. If the current node is a word end.
                2. And the current word is not the same as the input word.
                3. And the remaining of the input word is a palindrome.
                This means we have found a combination of palindrome pairs.

                For example: we have ['abxyx', 'ba'], the trie will be:

                      --- root ---
                      | a        | x
                      n1         n3
                      | b        | y
                      n2         n4
                                 | x
                                 n5
                                 | b
                                 n6
                                 | a
                                 n7

                So when we search for 'abxyx', we will first arrive at n2, which
                is a word end. It means there will be a 'ba' word in the input
                list. So we check if the remaining xyx is a palindrome, if so,
                combining abxyx and ba will create a new palindrome, which is
                the target pair we are looking for.
                """
                rslt.append([wordIdx, currNode.wordEndInd])

            if c not in currNode.nextNodes:  # Cannot go any further.
                return rslt

            currNode = currNode.nextNodes[c]

        """
        Now the currNode is pointing to the word end node for the current
        input word. Then we check if this node's pIdxs has any item. Those
        items could also form a palindrome with the whole contents of the
        current input word.
        """
        for pIdx in currNode.pIdxs:
            if pIdx != wordIdx:
                rslt.append([wordIdx, pIdx])

        return rslt


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        Presumption, all the characters in the input list are in lower cases.
        """
        rslt, trie = [], Trie()

        # First build a trie based on the input words.
        for wordIdx, word in enumerate(words):
            trie.add_word(word, wordIdx)

        # Then search for each word and get the palindrome pairs.
        for wordIdx, word in enumerate(words):
            rslt += trie.search_word(word, wordIdx)

        return rslt


print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
