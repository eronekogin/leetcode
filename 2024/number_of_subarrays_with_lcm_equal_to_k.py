"""
https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/
"""


from math import lcm


class Solution:
    """
    Solution
    """

    def subarray_lcm(self, nums: list[int], k: int) -> int:
        """
        subarray lcm
        """
        cnt = 0
        n = len(nums)
        for i in range(n):
            curr = 1
            for j in range(i, n):
                if k % nums[j] > 0:
                    break

                curr = lcm(curr, nums[j])
                cnt += curr == k

        return cnt
