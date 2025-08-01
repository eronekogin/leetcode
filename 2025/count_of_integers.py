"""
https://leetcode.com/problems/count-of-integers/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        """
        count
        """
        @cache
        def dp(position: int, is_tight: bool, curr_sum: int, nums: tuple):
            if curr_sum > max_sum:
                return 0

            if position == len(nums):
                return int(min_sum <= curr_sum <= max_sum)

            rslt = 0

            bound = nums[position] if is_tight else 10

            for i in range(bound):
                rslt = (rslt + dp(position + 1, False, curr_sum + i, nums)) % mod

            if bound < 10:
                rslt = (
                    rslt +
                    dp(position + 1, True, curr_sum + bound, nums)
                ) % mod

            return rslt % mod

        mod = 10 ** 9 + 7
        n1 = tuple(map(int, str(int(num1) - 1)))
        n2 = tuple(map(int, num2))

        return (dp(0, True, 0, n2) - dp(0, True, 0, n1)) % mod
