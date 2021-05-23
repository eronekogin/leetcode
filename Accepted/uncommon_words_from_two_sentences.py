"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""


from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        cnt = Counter(s1.split()) + Counter(s2.split())
        return [w for w, v in cnt.items() if v == 1]


print(Solution().uncommonFromSentences(
    "this apple is sweet", "this apple is sour"))
