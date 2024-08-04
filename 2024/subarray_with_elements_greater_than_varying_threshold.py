"""
https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/description/
"""


class Solution:
    """
    Solution
    """

    def valid_subarray_size(self, nums: list[int], threshold: int) -> int:
        """
        valid subarray size
        """
        nums = [0] + nums + [0]
        stack = [0]

        for i in range(1, len(nums)):
            while nums[i] < nums[stack[-1]]:
                curr = nums[stack.pop()]
                if curr > threshold / (i - stack[-1] - 1):
                    return i - stack[-1] - 1

            stack.append(i)

        return -1
