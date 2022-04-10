"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/
"""


from collections import Counter


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        cnt = Counter(arr)
        if 0 in cnt and cnt[0] > 1:
            return True

        return any(x * 2 in cnt for x in cnt if x)
