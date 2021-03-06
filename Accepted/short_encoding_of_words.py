"""
https://leetcode.com/problems/short-encoding-of-words/
"""


class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        """
        1. If the word is a suffix of another word, we don't need to count
            this word into the encoding.
        2. Then we could add each word into a trie in a reversed way and then
            count the total length of the leaves.
        """
        trie, rslt = {}, 0
        for w in words:
            node = trie
            for c in reversed(w):
                if '#' in node:  # Found a suffix.
                    rslt -= node.pop('#')

                node = node.setdefault(c, {})

                if not node:  # Found a new leaf.
                    node['#'] = len(w) + 1
                    rslt += node['#']

        return rslt
