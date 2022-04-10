"""
https://leetcode.com/problems/implement-trie-prefix-tree/

https://leetcode.com/articles/implement-trie-prefix-tree/
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        curr[' '] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr:
                return False

            curr = curr[c]

        return ' ' in curr

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False

            curr = curr[c]

        return True


t = Trie()
t.insert('apple')
t.search('apple')
