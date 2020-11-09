"""
https://leetcode.com/problems/replace-words/
"""


from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def build_tree(self, words: List[str]) -> None:
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr:
                    curr[c] = {}

                curr = curr[c]

            curr['#'] = True  # Mark word end.

    def search_prefix(self, word: str) -> str:
        curr = self.root
        for end, c in enumerate(word):
            if c not in curr:  # No match.
                return ''

            if '#' in curr[c]:  # Found the first word end.
                return word[:end + 1]

            curr = curr[c]

        return ''  # The current word is less than any root string.


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        trie.build_tree(dictionary)
        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.search_prefix(words[i]) or words[i]

        return ' '.join(words)


print(Solution().replaceWords(
    ["cat", "bat", "rat"], "the cattle was rattled by the battery"))
