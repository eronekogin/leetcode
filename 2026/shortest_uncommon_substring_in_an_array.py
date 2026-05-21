"""
https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/
"""

from collections import defaultdict


class TrieNode:
    """
    Trie Node
    """

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_num_contain = set()


class Trie:
    """
    Trie
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, num: int) -> None:
        """
        insert
        """
        n = len(word)
        for i in range(n):
            node = self.root
            for j in range(i, n):
                node = node.children[word[j]]
                node.word_num_contain.add(num)

    def search(self, word: str) -> str:
        """
        search
        """
        n = len(word)
        res = []
        for i in range(n):
            node = self.root
            cur_str = ""
            for j in range(i, n):
                cur_str += word[j]
                node = node.children[word[j]]
                if len(node.word_num_contain) == 1:
                    res.append(cur_str)
                    break

        if not res:
            return ''

        return sorted(res, key=lambda x: (len(x), x))[0]


class Solution:
    """
    Solution
    """

    def shortest_substrings(self, arr: list[str]) -> list[str]:
        """
        shortest substrings
        """
        t = Trie()
        for i, word in enumerate(arr):
            t.insert(word, i)

        return [t.search(word) for word in arr]
