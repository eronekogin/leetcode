"""
https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def beautiful_subarrays(self, nums: list[int]) -> int:
        """
        beautiful subarrays
        """
        cnt = Counter({0: 1})
        rslt = prev = 0

        for x in nums:
            prev ^= x
            rslt += cnt[prev]
            cnt[prev] += 1

        return rslt
