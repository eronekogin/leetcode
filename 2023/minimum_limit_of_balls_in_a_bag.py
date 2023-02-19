"""
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
"""


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = l + ((r - l) >> 1)

            # For each number in nums, in order to split it several bags with
            # maximum size as m, we need (num - 1) // m operations. then we
            # count the total number of operations needed and compare it with
            # maxOperations. if it exceeds the limit, it means m is too small
            # and we need bigger m, vice versa.
            if sum((num - 1) // m for num in nums) > maxOperations:
                l = m + 1
            else:
                r = m

        return l
