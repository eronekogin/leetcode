"""
https://leetcode.com/problems/longest-word-in-dictionary/
"""


from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        memo, rslt = set(), ''
        for w in sorted(words, key=lambda x: (len(x), x)):
            if len(w) == 1 or w[:-1] in memo:
                memo.add(w)
                if len(w) > len(rslt):
                    rslt = w

        return rslt


print(Solution().longestWord(
    ["a", "banana", "app", "appl", "ap", "apply", "apple"]))
