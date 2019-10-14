"""
https://leetcode.com/problems/word-ladder-ii/
"""


from typing import List


class Solution:
    def findLadders(
            self,
            beginWord: str,
            endWord: str,
            wordList: List[str]) -> List[List[str]]:
        """
        Using BFS solution.
        """
        if endWord not in wordList:
            return []

        wordSet, chars = set(wordList), 'abcdefghijklmnopqrstuvwxyz'
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            newLayer = {}
            for word in layer:
                if word == endWord:
                    return layer[word]  # All transformations are found.

                for i in range(len(word)):
                    for c in chars:
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordSet:
                            newLayer[newWord] = newLayer.get(newWord, []) + [
                                w + [newWord] for w in layer[word]]

            wordSet -= set(newLayer.keys())  # Remove the checked words.
            layer = newLayer

        return []  # No transformation is found.
