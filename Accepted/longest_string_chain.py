"""
https://leetcode.com/problems/longest-string-chain/
"""


from collections import Counter


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        """
        Sort the words by length, then for each word, try to remove 1 char
        from it and see if the updated words existed in the previous scanned
        words.
        """
        memo = Counter()
        for w in sorted(words, key=len):
            memo[w] = max(memo[w[:i] + w[i + 1:]] for i in range(len(w))) + 1

        return max(memo.values())
