"""
https://leetcode.com/problems/find-common-characters/
"""


from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        cnt = None
        for w in words:
            if cnt is None:
                cnt = Counter(w)
            else:
                cnt &= Counter(w)

        rslt = []
        for c, times in cnt.items():
            rslt.extend([c] * times)

        return rslt
