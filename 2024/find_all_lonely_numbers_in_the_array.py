"""
https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def find_lonely(self, nums: list[int]) -> list[int]:
        """
        find_lonely
        """
        cnt = Counter(nums)
        return [
            k
            for k, v in cnt.items()
            if v == 1 and k + 1 not in cnt and k - 1 not in cnt
        ]
