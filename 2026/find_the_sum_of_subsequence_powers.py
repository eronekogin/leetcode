"""
https://leetcode.com/problems/find-the-sum-of-subsequence-powers/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def sum_of_powers(self, nums: list[int], k: int) -> int:
        """
        sum of powers
        """
        @cache
        def dp(i: int, min_diff: int, last_picked: int, remain: int) -> int:
            if remain == 0:
                if min_diff != max_limit:
                    return min_diff

                return 0

            if i == len(nums):
                return 0

            pick_sum = dp(
                i + 1,
                min(min_diff, abs(last_picked - nums[i])),
                nums[i],
                remain - 1
            )

            not_pick_sum = dp(
                i + 1,
                min_diff,
                last_picked,
                remain
            )

            return (pick_sum + not_pick_sum) % m

        m = 10 ** 9 + 7
        nums.sort()  # sort first to ensure min diff
        max_limit = 10 ** 9
        return dp(0, max_limit, max_limit, k)
