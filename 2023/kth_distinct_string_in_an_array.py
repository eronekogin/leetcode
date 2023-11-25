"""
https://leetcode.com/problems/kth-distinct-string-in-an-array/
"""


class Solution:
    """
    Solution
    """

    def kth_distinct(self, arr: list[str], k: int) -> str:
        """
        kth_distinct
        """
        memo = {}
        for x in arr:
            memo[x] = x not in memo

        cnt = 0
        for x in arr:
            cnt += memo[x]
            if cnt == k:
                return x

        return ''
