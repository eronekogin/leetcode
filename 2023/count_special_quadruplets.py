"""
https://leetcode.com/problems/count-special-quadruplets/
"""

from collections import defaultdict


class Solution:
    """
    Define solution.
    """

    def count_quadruplets(self, nums: list[int]) -> int:
        """
        count quaduplates.
        """
        cnt = 0
        n = len(nums)
        seen: defaultdict[int, int] = defaultdict(int)

        for bc in range(1, n - 1):
            # Count d - c first, so that we don't count a + b + b = d case,
            # as c must be strictly greater than b.
            c = bc
            for d in range(c + 1, n):
                cnt += seen[nums[d] - nums[c]]

            # Count a + b.
            b = bc
            for a in range(b):
                seen[nums[a] + nums[b]] += 1

        return cnt
