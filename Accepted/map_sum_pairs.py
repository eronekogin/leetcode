"""
https://leetcode.com/problems/map-sum-pairs/
"""


class Trie:

    def __init__(self):
        self._root = {}

    def add_word(self, w: str, delta: int) -> None:
        currNode = self._root
        for c in w:
            currNode['#'] = currNode.get('#', 0) + delta
            if c not in currNode:
                currNode[c] = {}

            currNode = currNode[c]

        currNode['#'] = currNode.get('#', 0) + delta  # Mark word end.

    def sum_word_end(self, w: str) -> int:
        currNode = self._root
        for c in w:
            if c not in currNode:
                return 0

            currNode = currNode[c]

        return currNode['#']


class MapSum:

    def __init__(self):
        self._trie = Trie()
        self._memo = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self._memo.get(key, 0)
        self._memo[key] = val
        self._trie.add_word(key, delta)

    def sum(self, prefix: str) -> int:
        return self._trie.sum_word_end(prefix)


ms = MapSum()
ms.insert('apple', 3)
ms.sum('ap')
