"""
https://leetcode.com/problems/custom-sort-string/
"""


from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cnt = Counter(T)
        rslt = []
        for c in S:
            if cnt[c]:
                rslt += [c] * cnt[c]
                cnt[c] = 0

        for c in cnt:
            if cnt[c]:
                rslt += [c] * cnt[c]

        return ''.join(rslt)
