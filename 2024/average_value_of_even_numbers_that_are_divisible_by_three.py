"""
https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/
"""


class Solution:
    """
    Solution
    """

    def average_value(self, nums: list[int]) -> int:
        """
        average value
        """
        total = cnt = 0
        for x in nums:
            if x % 6 == 0:
                cnt += 1
                total += x

        if cnt == 0:
            return 0

        return total // cnt
