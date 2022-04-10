"""
https://leetcode.com/problems/prefix-and-suffix-search/
"""


from typing import List


class Trie:
    """
    Prefix tree.
    """

    def __init__(self):
        self._root = {}  # '#' marks the maximum index at the word end.

    def add_word(self, idx: int, w: str) -> None:
        currNode = self._root
        for c in w:
            if c not in currNode:
                currNode[c] = {}

            currNode = currNode[c]
            currNode['#'] = idx

        currNode['#'] = idx

    def search_word(self, w: str) -> int:
        currNode = self._root
        for c in w:
            if c not in currNode:
                return -1

            currNode = currNode[c]

        return currNode.get('#', -1)


class WordFilter:

    def __init__(self, words: List[str]):
        """
        For each word in words, add all its suffix + '=' + itself to the trie.
        Take word 'apple' as an example, what we need to add to the trie are
        '=apple', 'e=apple', 'le=apple', 'ple=apple', 'pple=apple',
        'apple=apple'. Then when we want to search the prefix and suffix
        combination, we could search using suffix + '=' + prefix.
        """
        self._trie = Trie()
        for idx, w in enumerate(words):
            for i in range(len(w)):
                self._trie.add_word(idx, w[i:] + '=' + w)

    def f(self, prefix: str, suffix: str) -> int:
        return self._trie.search_word(suffix + '=' + prefix)
