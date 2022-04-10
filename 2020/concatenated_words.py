"""
https://leetcode.com/problems/concatenated-words/
"""


from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def build_from_words(self, words: List[str]) -> None:
        for w in words:
            currNode = self.root
            for c in w:
                if c not in currNode:
                    currNode[c] = {}

                currNode = currNode[c]

            currNode['#'] = None  # Indicate the word end.

    def is_concatenated_word(self, w: str, start: int, preCnt: int) -> bool:
        if start == len(w):  # Arrives at the end.
            # Must have at least one pre word to concatenate.
            return preCnt > 1

        currNode = self.root
        for i in range(start, len(w)):
            if w[i] not in currNode:
                return False

            currNode = currNode[w[i]]

            # 1. Take the current word end and check if the remainig part is
            #   also a valid word in trie.
            # 2. Or simply ingore this word end and continue to find a latter
            #   one.
            if '#' in currNode and self.is_concatenated_word(
                    w, i + 1, preCnt + 1):
                return True

        return False  # Could not find a word end in trie for the input word.


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        1. First build a prefix tree based on the input words.
        2. Then use prefix tree to determine if a long word is concatenated
            by the previous small words by counting the total word end in the
            trie for the current word.
        """
        trie = Trie()
        trie.build_from_words(words)
        rslt = []
        for w in words:
            if trie.is_concatenated_word(w, 0, 0):
                rslt.append(w)

        return rslt

    def findAllConcatenatedWordsInADict2(self, words: List[str]) -> List[str]:
        """
        Simply brutal force with cache.
        """
        memo, wordSet = {}, set(words)

        def is_concatenated_word(w: str) -> bool:
            if w in memo:
                return memo[w]

            for i in range(1, len(w)):
                prefix, suffix = w[:i], w[i:]
                if (prefix in wordSet and suffix in wordSet) or (
                        prefix in wordSet and is_concatenated_word(suffix)):
                    memo[w] = True
                    return True

            memo[w] = False
            return False

        return [w for w in words if is_concatenated_word(w)]


print(Solution().findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
        "hippopotamuses", "rat", "ratcatdogcat"]
))
