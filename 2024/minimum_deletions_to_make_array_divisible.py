"""
https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/description/
"""


from math import gcd


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int], nums_divide: list[int]) -> int:
        """
        min operations
        """
        target = gcd(*nums_divide)
        visited: set[int] = set()
        deletes = 0
        for x in sorted(nums):
            if x not in visited:
                if target % x == 0:
                    return deletes

                visited.add(x)

            deletes += 1

        return -1
