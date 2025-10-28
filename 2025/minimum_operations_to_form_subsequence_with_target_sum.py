"""
https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int], target: int) -> int:
        """
        min operations
        """
        total = sum(nums)

        # All numbers cannot form to target
        if total < target:
            return -1

        nums.sort()
        operations = 0

        while target:
            x = nums.pop()
            if total - x >= target:
                # We can form with small digits
                total -= x
            elif x <= target:
                # Take the current number
                total -= x
                target -= x
            else:
                # Current number is too large, split it to small ones
                nums.append(x >> 1)
                nums.append(x >> 1)
                operations += 1

        return operations
