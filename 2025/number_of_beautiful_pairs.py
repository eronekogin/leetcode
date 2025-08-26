"""
https://leetcode.com/problems/number-of-beautiful-pairs/description/
"""


from math import gcd, log10


class Solution:
    """
    Solution
    """

    def count_beautiful_pairs(self, nums: list[int]) -> int:
        """
        count beautiful pairs
        """
        cnt = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                n = int(log10(nums[i]))
                cnt += gcd(nums[i] // 10 ** n, nums[j] % 10) == 1

        return cnt
