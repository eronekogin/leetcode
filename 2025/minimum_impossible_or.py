"""
https://leetcode.com/problems/minimum-impossible-or/description/
"""


class Solution:
    """
    Solution
    """

    def min_impossible_or(self, nums: list[int]) -> int:
        """
        min impossible or
        """
        memo = set(nums)
        for i in range(32):
            if (1 << i) not in memo:
                return 1 << i

        return -1


print(Solution().min_impossible_or([5, 3, 2]))
