"""
https://leetcode.com/problems/find-the-minimum-cost-array-permutation/description/
"""


from functools import cache
from math import inf


class Solution:
    """
    Solution
    """

    def find_permutation(self, nums: list[int]) -> list[int]:
        """
        rotating the rslt does not change the total score since
        shifting the rslt from left to right does not change
        the score of two adjacent numbers. So we can fix perm[0] to be 0
        to validate any perms that starts with 0 and has the
        minimum score and meanwhile is lexicalgraphcailly smallest
        """
        @cache
        def dp(mask: int, prev: int):
            if mask.bit_count() == n:
                return abs(prev - nums[0])

            min_score = inf
            min_num = -1
            for i in range(1, n):
                if not mask & (1 << i):
                    curr_score = (
                        dp(mask | (1 << i), i) +
                        abs(prev - nums[i])
                    )

                    if curr_score < min_score:
                        min_score = curr_score
                        min_num = i

            best_picks[prev][mask] = min_num

            return min_score

        n = len(nums)
        best_picks = [[0] * (1 << n) for _ in range(n)]
        dp(1, 0)

        rslt: list[int] = []
        mask = 1
        prev = 0
        for _ in range(n):
            rslt.append(prev)
            prev = best_picks[prev][mask]
            mask |= 1 << prev

        return rslt
