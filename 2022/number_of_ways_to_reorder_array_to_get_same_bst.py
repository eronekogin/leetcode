"""
https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
"""


from math import comb


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def f(nums: list[int]) -> int:
            if len(nums) <= 2:
                return 1

            left = [num for num in nums if num < nums[0]]
            right = [num for num in nums if num > nums[0]]

            return comb(len(left) + len(right), len(right)) * f(left) * f(right)

        # Subtract 1 from the result is because we don't count the
        # original order of nums.
        return (f(nums) - 1) % (10 ** 9 + 7)
